from fastapi.responses import StreamingResponse
from openrouter.errors import TooManyRequestsResponseError
from fastapi import APIRouter, HTTPException
from db import db
from agent import agent
from pydantic import BaseModel

router = APIRouter()


class ChatRequests(BaseModel):
    doc_id: str
    query: str


@router.post("/chat")
def chat(req: ChatRequests):
    source_path = "uploads/" + req.doc_id + ".pdf"

    if not req.doc_id or not req.query:
        raise HTTPException(status_code=400, detail="Please provide doc_id and query")

    try:

        docs = db().similarity_search(req.query, k=3, filter={"source": source_path})

        if not docs:
            raise HTTPException(
                status_code=404, detail="No file found. Please embed pdf first"
            )

        context = "\n\n".join([doc.page_content for doc in docs])

        def stream():
            for chunk in agent().stream({"context": context, "question": req.query}):
                yield chunk

        return StreamingResponse(stream(), media_type="text/event-stream")
    except TooManyRequestsResponseError as e:
        raise HTTPException(status_code=429, detail="Too many requests")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
