from contextlib import asynccontextmanager
from fastapi import FastAPI
import uvicorn
from routes import pdf_router
from agent import create_agents
from dotenv import load_dotenv

load_dotenv()

agent_executor = None


@asynccontextmanager
async def startup(app: FastAPI):
    global agent_executor
    agent_executor = create_agents()
    yield


app = FastAPI(lifespan=startup)


app.include_router(pdf_router, prefix="/api/pdf")


@app.get("/")
def main():
    return {"message": "Hello world"}


if __name__ == "__main__":
    uvicorn.run(app, port=8000)
