import os

from langchain_community.chat_models import ChatOllama
from langchain_community.embeddings import OllamaEmbeddings

import config, model

llm = model.get_llm()

res = llm.invoke("What is BTC?")

print(res)