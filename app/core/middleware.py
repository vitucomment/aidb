from starlette.middleware.base import BaseHTTPMiddleware
from app.db.postgres import get_connection

class ResourceMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        request.state.conn = get_connection()
        try:
            response = await call_next(request)
        finally:
            request.state.conn.close()  # Garante que a conexão será fechada
        return response