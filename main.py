from app.core.init_app import create_app
from app.core.middleware import ResourceMiddleware

app = create_app()
app.add_middleware(ResourceMiddleware)