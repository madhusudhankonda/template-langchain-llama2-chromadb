import os
from dotenv import load_dotenv

from langchain_community.chat_models import ChatOllama
from langchain_community.embeddings import OllamaEmbeddings
import config
load_dotenv()


MODEL = config.MODEL
OLLAMA_BASE_URL = config.OLLAMA_BASE_URL


def get_llm():
    llm = ChatOllama(base_url=OLLAMA_BASE_URL, model=MODEL)

    return llm

def get_embeddings():
    
    ollama_embeddings = OllamaEmbeddings(base_url=OLLAMA_BASE_URL, model=MODEL)
