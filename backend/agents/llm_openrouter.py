import os
from langchain_openrouter import ChatOpenRouter


def llm_openrouter():
    if not os.getenv("OPENROUTER_API_KEY"):
        raise ValueError("OPENROUTER_API_KEY not found")

    return ChatOpenRouter(
        model="meta-llama/llama-3.2-3b-instruct:free",
        temperature=0,
        max_tokens=512,
        max_retries=2,
    )
