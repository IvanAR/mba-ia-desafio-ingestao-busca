import os
import env  # noqa: F401
from langchain_postgres import PGVector
from embeddings import get_embeddings

PROMPT_TEMPLATE = """
CONTEXTO:
{context}

REGRAS:
- Responda somente com base no CONTEXTO.
- Se a informação não estiver explicitamente no CONTEXTO, responda:
  "Não tenho informações necessárias para responder sua pergunta."
- Nunca invente ou use conhecimento externo.
- Nunca produza opiniões ou interpretações além do que está escrito.

EXEMPLOS DE PERGUNTAS FORA DO CONTEXTO:
Pergunta: "Qual é a capital da França?"
Resposta: "Não tenho informações necessárias para responder sua pergunta."

Pergunta: "Quantos clientes temos em 2024?"
Resposta: "Não tenho informações necessárias para responder sua pergunta."

Pergunta: "Você acha isso bom ou ruim?"
Resposta: "Não tenho informações necessárias para responder sua pergunta."

PERGUNTA DO USUÁRIO:
{question}

RESPONDA A "PERGUNTA DO USUÁRIO"
"""


def search_prompt(q: str) -> str:
    embeddings = get_embeddings()
    store = PGVector(
        embeddings=embeddings,
        collection_name=env.PG_VECTOR_COLLECTION_NAME,
        connection=env.DATABASE_URL,
    )
    docs = store.similarity_search(q, k=5)
    c = "\n\n".join(doc.page_content for doc in docs)
    return PROMPT_TEMPLATE.format(context=c, question=q)
