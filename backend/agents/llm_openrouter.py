import os
from langchain_openrouter import ChatOpenRouter


def llm_openrouter():
    if not os.getenv("OPENROUTER_API_KEY"):
        raise ValueError("OPENROUTER_API_KEY not found")

    llm = ChatOpenRouter(model="qwen/qwen3.6-plus-preview:free")

    return llm
