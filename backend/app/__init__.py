from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from contextlib import asynccontextmanager
import logging

from app.config import current_config
from app.database import init_db
from app.api import routes, websocket

# Setup logging
logging.basicConfig(
    level=current_config.LOG_LEVEL,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
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
        lifespan=lifespan
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
        allowed_hosts=["localhost", "127.0.0.1"]
    )
    
    # Include routers
    app.include_router(routes.router, prefix=current_config.API_V1_STR)
    app.include_router(websocket.router, prefix=current_config.API_V1_STR)
    
    # Health check endpoint
    @app.get("/health")
    async def health_check():
        return {
            "status": "healthy",
            "version": "1.0.0",
            "environment": current_config.__class__.__name__
        }
    
    # Root endpoint
    @app.get("/")
    async def root():
        return {
            "message": "AI Learning Machine API",
            "docs": "/docs",
            "version": "1.0.0"
        }
    
    logger.info(f"Application initialized in {current_config.__class__.__name__} mode")
    return app


app = create_app()
