from contextlib import asynccontextmanager
from fastapi import FastAPI
import uvicorn
from routes import pdf_router, chat_router
from agent import agent
from dotenv import load_dotenv

load_dotenv()

agent_executor = None

app = FastAPI()


app.include_router(pdf_router, prefix="/api/pdf")
app.include_router(chat_router, prefix="/api/ai")

if __name__ == "__main__":
    uvicorn.run(app, port=8000)
