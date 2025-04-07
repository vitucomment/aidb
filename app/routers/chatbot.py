from fastapi import APIRouter, Body, Depends
from langchain_ollama import ChatOllama
from app.core.llm.ollama import get_llm, get_embeddings
from langchain_community.embeddings import OllamaEmbeddings
from app.services.chatbot import run_chat
from fastapi import Request

router = APIRouter()

from fastapi import Request
@router.post("/chat", tags=["Chatbot"])
async def chat_with_llm(request: Request, prompt: str = Body(..., embed=True)):
    agent = request.app.state.agent
    return run_chat(prompt, agent)
