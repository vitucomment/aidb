from fastapi import FastAPI

from app.routers import health
from app.routers import chatbot

from app.core.llm.ollama import init_ollama_llm, init_ollama_embeddinng

from app.services.agents.supervisor import create_chat_assistant


def create_app() -> FastAPI:
    app = FastAPI()
    
    # Resourcers
    app.state.llm = init_ollama_llm()
    app.state.embeddings = init_ollama_embeddinng()
    
    
    # Agents
    app.state.agent = create_chat_assistant(app.state.llm)
    
    
    # Routers
    app.include_router(health.router)
    app.include_router(chatbot.router)
    return app
