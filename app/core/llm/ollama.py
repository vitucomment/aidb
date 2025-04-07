from langchain_ollama import ChatOllama
from langchain_ollama import OllamaEmbeddings

from fastapi import Request, Depends

def init_ollama_llm():
    """Initialize the Ollama LLM."""
    print("Initializing Ollama LLM...")    
    llm = ChatOllama(model="llama3.1", temperature=0.7)
    return llm

def get_llm(request: Request) -> ChatOllama:
    return request.app.state.llm

def init_ollama_embeddinng():
    """Initialize the Ollama Embeddings."""
    print("Initializing Ollama Embeddings...")    
    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    return embeddings

def get_embeddings(request: Request) -> OllamaEmbeddings:
    return request.app.state.embeddings