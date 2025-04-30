#!/bin/bash

# navigate to /path/to/your/script
# chmod +x run.sh   
# ./run.sh      

# Colors for output
GREEN='\033[0c;32m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Function to print colored messages
print_message() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Check if Python virtual environment is activated
if [ -z "$VIRTUAL_ENV" ]; then
    print_message "Activating Python virtual environment..."
    if [ -d "venv" ]; then
        source venv/bin/activate
    else
        print_error "Virtual environment not found. Please create it first with: python -m venv venv"
        exit 1
    fi
fi

# Check if required Python packages are installed
print_message "Checking Python dependencies..."
if ! pip show flask flask-cors python-dotenv > /dev/null 2>&1; then
    print_message "Installing required Python packages..."
    pip install -r requirements.txt
fi

# Function to cleanup processes on exit
cleanup() {
    print_message "Shutting down servers..."
    kill $(jobs -p) 2>/dev/null
    exit 0
}

# Set up trap to catch termination signals
trap cleanup SIGINT SIGTERM

# Start Flask backend server
print_message "Starting Flask backend server..."
python app/main.py &
FLASK_PID=$!

# Wait a moment for Flask to start
sleep 2

# Check if Flask server started successfully
if ! kill -0 $FLASK_PID 2>/dev/null; then
    print_error "Failed to start Flask server"
    exit 1
fi

# Start UI server
print_message "Starting UI server..."
cd ui && python -m http.server 8080 &
UI_PID=$!

# Wait a moment for UI server to start
sleep 1

# Check if UI server started successfully
if ! kill -0 $UI_PID 2>/dev/null; then
    print_error "Failed to start UI server"
    kill $FLASK_PID
    exit 1
fi

print_message "Both servers are running!"
print_message "Backend API: http://localhost:5010"
print_message "UI: http://localhost:8080"
print_message "Press Ctrl+C to stop both servers"

# Keep script running and wait for user interrupt
wait 