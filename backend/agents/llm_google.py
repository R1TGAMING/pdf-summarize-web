import os
from langchain_google_genai import GoogleGenerativeAI


def llm_google():
    if not os.getenv("GOOGLE_API_KEY"):
        raise ValueError("GOOGLE_API_KEY not found")

    return GoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0,
        max_tokens=512,
        max_retries=2,
    )
