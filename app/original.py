from flask import Flask, request, jsonify
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Google Translate API configuration
GOOGLE_TRANSLATE_API_KEY = os.getenv('GOOGLE_TRANSLATE_API_KEY')
GOOGLE_TRANSLATE_API_URL = 'https://translation.googleapis.com/language/translate/v2'

@app.route('/api/greet', methods=['POST'])
def greet():
    try:
        # Get JSON data from request
        data = request.get_json()
        
        # Validate input
        if not data:
            return jsonify({'error': 'No data provided'}), 400
            
        # Get name with default value
        name = data.get('name', 'World')
        
        # Get language with default value
        language = data.get('language', 'en')
        
        # If language is not English, translate the greeting
        if language != 'en':
            if not GOOGLE_TRANSLATE_API_KEY:
                return jsonify({'error': 'Translation API key not configured'}), 500
                
            # Prepare translation request
            translation_data = {
                'q': f'Hello, {name}!',
                'source': 'en',
                'target': language,
                'key': GOOGLE_TRANSLATE_API_KEY
            }
            
            # Make translation request
            try:
                response = requests.post(GOOGLE_TRANSLATE_API_URL, data=translation_data)
                response.raise_for_status()
                translation = response.json()['data']['translations'][0]['translatedText']
                return jsonify({'message': translation})
            except requests.exceptions.RequestException as e:
                return jsonify({'error': f'Translation failed: {str(e)}'}), 500
        
        # Return default English greeting
        return jsonify({'message': f'Hello, {name}!'})
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True) 