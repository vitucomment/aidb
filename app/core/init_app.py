from fastapi import FastAPI

from app.routers import health
from app.routers import chatbot

from app.core.llm.ollama import init_ollama_llm, init_ollama_embeddinng
from app.db.postgres import create_chat_history_table, init_psycopg_connection

from app.services.agents.supervisor import create_chat_assistant


# app/core/init_app.py


def create_app() -> FastAPI:
    app = FastAPI()

    # Recursos
    app.state.llm = init_ollama_llm()
    app.state.embeddings = init_ollama_embeddinng()
    app.state.conn = init_psycopg_connection()
    app.state.agent = create_chat_assistant(app.state.llm)
    # Criação da tabela de histórico (só precisa ser chamada uma vez)
    create_chat_history_table(app.state.conn)

    # Rotas
    app.include_router(health.router)
    app.include_router(chatbot.router)

    return app
