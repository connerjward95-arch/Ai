#!/usr/bin/env python
"""Application entry point"""

import uvicorn
import logging
from app import create_app
from app.config import current_config

logging.basicConfig(
    level=current_config.LOG_LEVEL,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


if __name__ == "__main__":
    logger.info(f"Starting AI Learning Machine in {current_config.__class__.__name__} mode")
    
    app = create_app()
    
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=5000,
        reload=current_config.DEBUG,
        log_level=current_config.LOG_LEVEL.lower()
    )
