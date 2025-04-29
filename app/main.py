# Import necessary libraries for Flask application 
from flask import Flask, request, jsonify

# and environment variable management
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize the Flask application
app = Flask(__name__)

# Google Translate API configuration
GOOGLE_TRANSLATE_API_KEY = os.getenv('GOOGLE_TRANSLATE_API_KEY')
GOOGLE_TRANSLATE_API_URL = 'https://translation.googleapis.com/language/translate/v2'

@app.route('/')
def index():
    return jsonify({
        'endpoints': {
            '/api/greet': {
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

        # Return default Enlgish greeting
        if language == 'en':
            greeting = f"Hello, {name}!"
        else:
            # Translate the greeting to the target language
            # TODO: Implement translation of the greeting to the target language if it is not English
            greeting = f"Hello, {name}!"

        return jsonify({'greeting': greeting})
    
    except Exception as e:
        return jsonify({'error': 'That did not work!', 'details': str(e)}), 500
    
    if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5001, debug=True)
