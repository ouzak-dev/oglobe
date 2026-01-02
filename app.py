"""
Flask Application Entry Point (Development)

For development: python app.py
For production: use wsgi.py with a WSGI server like Gunicorn
"""
from app import app

if __name__ == "__main__":
    # Development server - NOT for production use
    app.run(debug=True, host='0.0.0.0', port=5000)

