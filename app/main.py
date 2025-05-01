# Import necessary libraries for Flask application 
from flask import Flask, request, jsonify

# and environment variable management
import os
from dotenv import load_dotenv
from app.config import FLASK_ENV, GOOGLE_TRANSLATE_API_KEY, TRUSTED_ORIGIN 

# Initialize the Flask application
app = Flask(__name__)

# and browser security
from flask_cors import CORS
CORS(
    app,
    origins=[TRUSTED_ORIGIN],
    supports_credentials=True,
    methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["Content-Type", "Authorization"],
)

# and configure logging
import logging
logging.basicConfig(level=logging.DEBUG, 
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger('werkzeug')
logger.setLevel(logging.DEBUG)

# Google Translate API configuration
GOOGLE_TRANSLATE_API_KEY = GOOGLE_TRANSLATE_API_KEY
GOOGLE_TRANSLATE_API_URL = 'https://translation.googleapis.com/language/translate/v2'

@app.route('/')
def index():
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
        # Extract JSON data from request
        data = request.get_json()

        # Validate input
        if not data:
            return jsonify({'error': 'Please provide a JSON body with name and language'}), 400

        # Get name with 'World' asdefault value
        name = data.get('name', 'World')

        # Get language with 'en' as default value
        language = data.get('language', 'en')

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
            # Translate the greeting to the target language
            # TODO: Implement translation of the greeting to the target language if it is not English
            greeting = f"Hello, {name}!"

        app.logger.info('Request to root endpoint')
        return jsonify({'greeting': greeting})
    
    except Exception as e:
        app.logger.info('Request to root endpoint')
        return jsonify({'error': 'That did not work!', 'details': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5010, debug=True)
