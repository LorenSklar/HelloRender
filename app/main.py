# Import necessary libraries for Flask application 
from flask import Flask, request, jsonify

# and environment variable management
import os
from dotenv import load_dotenv
from config import FLASK_ENV, GOOGLE_TRANSLATE_API_KEY, TRUSTED_ORIGIN 

# Initialize the Flask application
app = Flask(__name__)

# Configure logging
import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Log the current environment and trusted origin
logger.debug(f"Current FLASK_ENV: {FLASK_ENV}")
logger.debug(f"Current TRUSTED_ORIGIN: {TRUSTED_ORIGIN}")

# and browser security
from flask_cors import CORS
CORS(
    app,
    origins=[TRUSTED_ORIGIN],
    supports_credentials=True,
    methods=["GET", "POST"],
    allow_headers=["Content-Type", "Authorization"],
)

# Google Translate API configuration
# GOOGLE_TRANSLATE_API_KEY = GOOGLE_TRANSLATE_API_KEY
# GOOGLE_TRANSLATE_API_URL = 'https://translation.googleapis.com/language/translate/v2'

@app.route('/')
def index():
    logger.info(f"Root endpoint accessed from: {request.origin}")
    return jsonify({
        'endpoints': {
            '/api/v1/greet': {
                'method': 'POST',
                'example_input': {
                    'name': 'John',
                    'language': 'es'
                }
            }
        }
    })

@app.route('/api/v1/greet', methods=['POST'])
def greet():
    try:
        # Log request source
        logger.info(f"Greeting request from: {request.origin}")
        logger.debug(f"Request headers: {dict(request.headers)}")

        # Extract JSON data from request
        data = request.get_json()
        logger.info(f"Request payload: {data}")

        # Validate input
        if not data:
            logger.warning("Empty request body received")
            return jsonify({'error': 'Please provide a JSON body with name and language'}), 400

        # Get name with 'World' as default value
        name = data.get('name', 'World')
        language = data.get('language', 'en')
        
        logger.info(f"Processing greeting - Name: {name}, Language: {language}")

        if language == 'en':
            greeting = f"Hello, {name}!"
        elif language == 'fr':
            greeting = f"Bonjour, {name}!"
        elif language == 'es':
            greeting = f"Hola, {name}!"
        elif language == 'it':
            greeting = f"Ciao, {name}!"
        elif language == 'de':
            greeting = f"Hallo, {name}!"
        else:
            greeting = f"Hello, {name}!"

        logger.info(f"Sending greeting: {greeting}")
        return jsonify({'greeting': greeting})
    
    except Exception as e:
        logger.error(f"Error processing request: {str(e)}", exc_info=True)
        return jsonify({'error': 'That did not work!', 'details': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5010, debug=True)
