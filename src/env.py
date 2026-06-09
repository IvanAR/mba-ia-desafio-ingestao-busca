import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+psycopg://postgres:postgres@localhost:5432/rag")
PG_VECTOR_COLLECTION_NAME = os.getenv("PG_VECTOR_COLLECTION_NAME", "documents")
PDF_PATH = os.getenv("PDF_PATH", "document.pdf")

for _var in ("REQUESTS_CA_BUNDLE", "GRPC_DEFAULT_SSL_ROOTS_FILE_PATH"):
    _val = os.getenv(_var)
    if _val:
        os.environ[_var] = os.path.expanduser(_val)
