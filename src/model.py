import os
from langchain.chat_models import init_chat_model
from langchain_core.language_models import BaseChatModel

GEMINI_MODEL = os.getenv("GEMINI_CHAT_MODEL", "gemini-2.0-flash-lite")

def get_chat_model() -> BaseChatModel:
    """Returns the configured chat model as a LangChain BaseChatModel instance.

    Centralises chat model creation so callers are decoupled from the specific
    provider. Swap the provider or model here and all dependants pick it up automatically.
    """
    return init_chat_model(model=GEMINI_MODEL, model_provider="google_genai", transport="rest")
