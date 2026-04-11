from langchain_core.documents import Document
import tempfile
from fastapi import APIRouter, UploadFile, HTTPException
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from db import db
from uuid import uuid4
import os
from pydantic import BaseModel


router = APIRouter()


class UploadRequests(BaseModel):
    file: UploadFile


@router.post("/upload")
async def upload_pdf(req: UploadRequests):
    os.makedirs("uploads", exist_ok=True)

    try:
        if req.file.content_type != "application/pdf":
            raise HTTPException(
                status_code=400, detail="Please upload a valid pdf file"
            )

        if not req.file.filename.endswith(".pdf"):
            raise HTTPException(status_code=400, detail="FIle must be .pdf")

        file_id = str(uuid4())
        file_path = os.path.join("uploads", file_id + ".pdf")

        with open(file_path, "wb") as f:
            f.write(await req.file.read())

        return {"message": "PDF uploaded successfully", "file_id": file_id}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/embed")
def embed_pdf(doc_id: str):
    try:
        file_path = f"uploads/{doc_id}.pdf"

        if not os.path.exists(file_path):
            raise HTTPException(
                status_code=404, detail="File not found. please upload pdf first"
            )

        reader = PyPDFLoader(file_path)

        pages = reader.load_and_split(
            text_splitter=RecursiveCharacterTextSplitter(
                chunk_size=256, chunk_overlap=64
            )
        )

        db().add_documents(pages)

        return {
            "message": "PDF embedded successfully",
            "pages": len(pages),
            "chunks": len(pages),
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
