from fastapi import FastAPI

from app.api.router import api_router
from app.core.settings import settings

def create_app() -> FastAPI:

    app = FastAPI(
        title=settings.APP_NAME,
        version=settings.APP_VERSION,
        description="Enterprise Agentic AI Assistant",
        docs_url="/docs",
        redoc_url="/redoc",
    )

    app.include_router(api_router)

    return app


app = create_app()
