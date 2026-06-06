from pathlib import Path
import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from app.config import current_config
from app.database import init_db
from app.api import routes, websocket

# Setup logging
logging.basicConfig(
    level=current_config.LOG_LEVEL,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Manage application lifespan"""
    # Startup
    logger.info("Starting AI Learning Machine...")
    init_db()

    yield

    # Shutdown
    logger.info("Shutting down AI Learning Machine...")


def create_app() -> FastAPI:
    """Create and configure FastAPI application"""

    app = FastAPI(
        title="AI Learning Machine",
        description="Interactive AI with continuous learning capabilities",
        version="1.0.0",
        lifespan=lifespan,
    )

    # CORS Middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=current_config.CORS_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Trusted Host Middleware
    app.add_middleware(
        TrustedHostMiddleware,
        allowed_hosts=["localhost", "127.0.0.1"],
    )

    # Include routers
    app.include_router(routes.router, prefix=current_config.API_V1_STR)
    app.include_router(websocket.router, prefix=current_config.API_V1_STR)

    # Mount built frontend if available
    frontend_build_dir = Path(__file__).resolve().parents[2] / "frontend" / "build"
    if frontend_build_dir.exists():
        app.mount(
            "/static",
            StaticFiles(directory=str(frontend_build_dir / "static")),
            name="static",
        )

        @app.get("/", include_in_schema=False)
        async def root_spa():
            return FileResponse(frontend_build_dir / "index.html")

        @app.get("/{full_path:path}", include_in_schema=False)
        async def spa_fallback(full_path: str):
            return FileResponse(frontend_build_dir / "index.html")

    else:
        @app.get("/", include_in_schema=False)
        async def root():
            return {
                "message": "AI Learning Machine API",
                "docs": "/docs",
                "version": "1.0.0",
            }

    @app.get("/health")
    async def health_check():
        return {
            "status": "healthy",
            "version": "1.0.0",
            "environment": current_config.__class__.__name__,
        }

    logger.info(
        "Application initialized in "
        f"{current_config.__class__.__name__} mode"
    )
    return app


app = create_app()
