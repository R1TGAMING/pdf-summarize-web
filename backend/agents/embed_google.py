import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings


def embed_google():
    if not os.getenv("GOOGLE_API_KEY"):
        raise ValueError("GOOGLE_API_KEY is not set")

    return GoogleGenerativeAIEmbeddings(model="gemini-embedding-2-preview")
