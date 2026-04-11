from langchain_chroma import Chroma
from agents import embed_google


def db():
    embeddings = embed_google()

    return Chroma(
        collection_name="pdf",
        persist_directory="./vectors",
        embedding_function=embeddings,
    )
