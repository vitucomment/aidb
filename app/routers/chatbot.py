from fastapi import APIRouter, Body, Request
from app.services.chatbot import run_chat

router = APIRouter()


@router.post("/chat", tags=["Chatbot"])
async def chat_with_llm(
    request: Request,
    prompt: str = Body(..., embed=True),
    session_id: str = Body(..., embed=True)
):
    """
    Endpoint para interação com o chatbot.

    Args:
        request (Request): Objeto de requisição FastAPI.
        prompt (str): Mensagem enviada pelo usuário.
        session_id (str): Identificador único da sessão do usuário.

    Returns:
        dict: Resposta gerada pelo chatbot.
    """
    agent = request.app.state.agent
    conn = request.app.state.conn
    return await run_chat(prompt, session_id, agent, conn)