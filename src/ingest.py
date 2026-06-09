import os
import env  # noqa: F401
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_postgres import PGVector
from embeddings import get_embeddings

def ingest_pdf():
    if not env.DATABASE_URL:
        raise SystemExit("DATABASE_URL is not set. Stopping application.")
    
    if not os.path.exists(env.PDF_PATH):
        raise SystemExit(f"PDF file not found: {env.PDF_PATH}. Stopping application.")
    
    print(f"Loading PDF: {env.PDF_PATH}")
    loader = PyPDFLoader(env.PDF_PATH)
    documents = loader.load()
    print(f"{len(documents)} page(s) loaded(s).")

    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
    chunks = splitter.split_documents(documents)
    print(f"{len(chunks)} generated chunks.")

    embeddings = get_embeddings()

    print("inserting vectors in pgVector...")
    PGVector.from_documents(
        documents=chunks,
        embedding=embeddings,
        collection_name=env.PG_VECTOR_COLLECTION_NAME,
        connection=env.DATABASE_URL,
        pre_delete_collection=False,
    )
    print("Ingestion concluded.")

if __name__ == "__main__":
    ingest_pdf()
