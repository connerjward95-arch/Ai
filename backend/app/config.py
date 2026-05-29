import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Base configuration"""
    
    # Flask/FastAPI
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')
    
    # Database
    DATABASE_URL = os.getenv(
        'DATABASE_URL',
        'postgresql://user:password@localhost:5432/ai_learning_machine'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Redis
    REDIS_URL = os.getenv('REDIS_URL', 'redis://localhost:6379/0')
    
    # JWT
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'jwt-secret-key')
    JWT_ALGORITHM = 'HS256'
    JWT_EXPIRATION_HOURS = 24
    
    # AI Configuration
    AI_MODEL_TYPE = os.getenv('AI_MODEL_TYPE', 'advanced')
    LEARNING_RATE = float(os.getenv('LEARNING_RATE', 0.8))
    MAX_MEMORY_CAPACITY = int(os.getenv('MAX_MEMORY_CAPACITY', 1000))
    RESPONSE_TIMEOUT_MS = int(os.getenv('RESPONSE_TIMEOUT_MS', 5000))
    
    # Paths
    MODEL_PATH = os.path.join(os.path.dirname(__file__), '../models')
    DATA_PATH = os.path.join(os.path.dirname(__file__), '../data')
    LOG_PATH = os.path.join(os.path.dirname(__file__), '../logs')
    
    # Embeddings
    EMBEDDING_MODEL = os.getenv('EMBEDDING_MODEL', 'all-MiniLM-L6-v2')
    VECTOR_DB_TYPE = os.getenv('VECTOR_DB_TYPE', 'pinecone')
    
    # API
    API_V1_STR = '/api/v1'
    CORS_ORIGINS = os.getenv('CORS_ORIGINS', 'http://localhost:3000').split(',')
    
    # Logging
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
    

class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    LOG_LEVEL = 'DEBUG'


class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    DATABASE_URL = os.getenv('DATABASE_URL')
    REDIS_URL = os.getenv('REDIS_URL')


class TestingConfig(Config):
    """Testing configuration"""
    TESTING = True
    DATABASE_URL = 'sqlite:///test.db'
    REDIS_URL = 'redis://localhost:6379/1'


# Configuration selector
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}

# Get config based on environment
env = os.getenv('FLASK_ENV', 'development')
current_config = config.get(env, config['default'])
