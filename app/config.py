import os
from dotenv import load_dotenv
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Load environment variables from .env file
load_dotenv()

# Flask environment
FLASK_ENV = os.getenv('FLASK_ENV', 'development')
if FLASK_ENV == 'development':
    FLASK_DEBUG = True
else:
    FLASK_DEBUG = False

logger.debug(f"FLASK_ENV: {FLASK_ENV}")

# API settings
GOOGLE_TRANSLATE_API_KEY = os.getenv('GOOGLE_TRANSLATE_API_KEY', '')

# Security settings
TRUSTED_ORIGIN = os.getenv('TRUSTED_ORIGIN_FOR_PRODUCTION', 'https://hellorendergreeting.onrender.com')
logger.debug(f"TRUSTED_ORIGIN: {TRUSTED_ORIGIN}")

