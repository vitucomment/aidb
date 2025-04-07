from fastapi import APIRouter, Body, Depends
from langchain_ollama import ChatOllama
from app.core.llm.ollama import get_llm, get_embeddings
from langchain_community.embeddings import OllamaEmbeddings
from app.services.chatbot import run_chat
from fastapi import Request

router = APIRouter()


@router.post("/chat", tags=["Chatbot"])
async def chat_with_llm(
    request: Request,
    prompt: str = Body(..., embed=True),
    session_id: str = Body(..., embed=True)
):
    agent = request.app.state.agent
    conn = request.app.state.conn
    return await run_chat(prompt, session_id, agent, conn)

