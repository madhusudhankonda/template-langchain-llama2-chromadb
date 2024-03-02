import os
from dotenv import load_dotenv

load_dotenv()

MODEL = os.getenv("MODEL")
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL")


def get_llm():
    llm = ChatOllama(base_url=OLLAMA_BASE_URL, model=MODEL)

    return llm

def get_embeddings():
    
    ollama_embeddings = OllamaEmbeddings(base_url=OLLAMA_BASE_URL, model=MODEL)

