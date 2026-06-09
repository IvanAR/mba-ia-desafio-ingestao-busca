import os
from langchain_core.embeddings import Embeddings
from langchain_google_genai import GoogleGenerativeAIEmbeddings

GOOGLE_EMBEDDING_MODEL = os.getenv("GOOGLE_EMBEDDING_MODEL", "gemini-embedding-001")

def get_embeddings() -> Embeddings:
    """Returns the configured embedding model as a LangChain Embeddings instance.

    Centralises embedding creation so ingest and search always use the same model
    without coupling either module to a specific provider implementation.
    Swap the provider here and both pipelines pick it up automatically.
    """
    return GoogleGenerativeAIEmbeddings(model=GOOGLE_EMBEDDING_MODEL, transport="rest")
