from fastapi import FastAPI
from app.core.config import settings

def create_app() -> FastAPI:
    app = FastAPI(title=settings.app_name)

    # Aqui você pode adicionar rotas:
    # from app.services import router as service_router
    # app.include_router(service_router)

    return app
