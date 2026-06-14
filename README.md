# Desafio MBA Engenharia de Software com IA - Full Cycle

Pipeline de RAG (Retrieval-Augmented Generation) que ingere um PDF em um banco vetorial PostgreSQL e responde perguntas com base exclusivamente no conteúdo do documento.

## Requisitos

- Python 3.11+
- Docker e Docker Compose (para o PostgreSQL com pgvector)
- Chave de API do Google Gemini (`GOOGLE_API_KEY`)

## Configuração

### 1. Banco de dados

Suba o PostgreSQL com a extensão pgvector via Docker Compose:

```bash
docker compose up -d
```

Isso cria o banco `rag` na porta `5432` com o usuário `postgres` e a extensão `vector` habilitada automaticamente.

### 2. Ambiente Python

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 3. Variáveis de ambiente

Copie o arquivo de exemplo e preencha os valores:

```bash
cp .env.example .env
```

Edite o `.env` e defina ao menos `GOOGLE_API_KEY`. As demais variáveis já possuem valores padrão compatíveis com o Docker Compose.

| Variável | Descrição | Padrão |
|---|---|---|
| `GOOGLE_API_KEY` | Chave da API Google Gemini | — |
| `GOOGLE_EMBEDDING_MODEL` | Modelo de embeddings | `gemini-embedding-2` |
| `GEMINI_CHAT_MODEL` | Modelo de chat | `gemini-3-flash-preview` |
| `DATABASE_URL` | URL de conexão PostgreSQL | `postgresql+psycopg://postgres:postgres@localhost:5432/rag` |
| `PG_VECTOR_COLLECTION_NAME` | Nome da coleção vetorial | `documents` |
| `PDF_PATH` | Caminho para o PDF a ser ingerido | `document.pdf` |

## Execução

### Passo 1 — Ingestão do PDF

Processa o PDF, divide em chunks e armazena os vetores no PostgreSQL:

```bash
python src/ingest.py
```

O script carrega o arquivo definido em `PDF_PATH`, gera embeddings e persiste na coleção `PG_VECTOR_COLLECTION_NAME`. Execute novamente apenas se o documento mudar.

### Passo 2 — Chat

Inicia o chat interativo no terminal:

```bash
python src/chat.py
```

## Comportamento do chat

O modelo responde **somente com base no conteúdo do PDF ingerido**. Para cada pergunta, o sistema busca os 5 trechos mais relevantes por similaridade vetorial e os envia como contexto ao Gemini.

Perguntas fora do escopo do documento recebem a resposta:

> "Não tenho informações necessárias para responder sua pergunta."

Para encerrar o chat, digite `exit`.
