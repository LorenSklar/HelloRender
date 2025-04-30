# Greeting App

A simple full-stack application that demonstrates basic API communication and translation features.

## Project Structure

```
.
├── app/
│   ├── main.py          # Flask backend
│   └── config.py        # Configuration settings
├── ui/
│   ├── index.html       # Frontend UI
│   ├── styles.css       # Frontend styles
│   └── script.js        # Frontend JavaScript
├── .env                 # Environment variables (create from .env.example)
├── .env.example         # Example environment variables
└── requirements.txt     # Python dependencies
```

## Local Development Setup

### 1. Backend Setup

1. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
cp .env.example .env
```
Edit `.env` and add your Google Translate API key.

4. Run the Flask backend:
```bash
python app/main.py
```
The backend will run on http://localhost:5010

### 2. Frontend Setup

To run the frontend separately:

1. Navigate to the `ui` directory:
```bash
cd ui
```

2. Start a simple HTTP server:
```bash
python -m http.server 8080
```

3. Access the frontend at http://localhost:8080

### 3. CORS Configuration

When running frontend and backend on different ports:

1. Update your `.env` file to include both origins:
```
TRUSTED_ORIGINS_DEVELOPMENT=http://localhost:5010,http://localhost:8080
```

2. The frontend JavaScript is configured to make requests to `http://localhost:5010/api/v1/greet`

3. If you change the backend port, update both:
   - The port in `script.js`
   - The port in your `.env` file

## Testing the Application

1. Start the backend (http://localhost:5010)
2. Start the frontend (http://localhost:8080)
3. Open http://localhost:8080 in your browser
4. Enter a name (optional, defaults to "World")
5. Select a language
6. Click "Get Greeting"

## API Endpoints

### POST /api/v1/greet
Request body:
```json
{
    "name": "John",  // optional, defaults to "World"
    "language": "es" // optional, defaults to "en"
}
```

Response:
```json
{
    "message": "¡Hola, John!"
}
```

## Troubleshooting

### CORS Issues
If you see CORS errors in the browser console:
1. Check that both frontend and backend origins are in `TRUSTED_ORIGINS_DEVELOPMENT` in `.env`
2. Ensure the backend is running on port 5010
3. Ensure the frontend is running on port 8080
4. Check that the fetch URL in `script.js` matches your backend URL

### API Key Issues
If translation fails:
1. Verify your Google Translate API key in `.env`
2. Check the backend logs for specific error messages

## Development Notes

- The backend runs in debug mode locally
- CORS is configured to allow requests from both frontend and backend origins
- Environment variables are loaded from `.env`
- Frontend and backend run on different ports for development

## Next Steps

1. Add error handling for API failures
2. Implement frontend validation
3. Add loading states and better error messages
4. Set up automated testing


