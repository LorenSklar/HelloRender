import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Flask environment
FLASK_ENV = os.getenv('FLASK_ENV', 'development')
if FLASK_ENV == 'development':
    FLASK_DEBUG = True
else:
    FLASK_DEBUG = False


# API settings
GOOGLE_TRANSLATE_API_KEY = os.getenv('GOOGLE_TRANSLATE_API_KEY', '')

# Security settings
TRUSTED_ORIGIN = {
    'development': os.getenv('TRUSTED_ORIGIN_FOR_DEVELOPMENT', 'http://localhost:8080'),
    'testing': os.getenv('TRUSTED_ORIGIN_FOR_TESTING', 'http://localhost:9090'),
    'production': os.getenv('TRUSTED_ORIGIN_FOR_PRODUCTION', 'https://your-production-domain.com')
}[FLASK_ENV]

