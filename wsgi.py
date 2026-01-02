"""
WSGI entry point for the Flask application.
This file exposes the Flask app as a WSGI callable for production servers
like Gunicorn, uWSGI, or deployment platforms.

Usage examples:
  - Gunicorn: gunicorn wsgi:app
  - uWSGI: uwsgi --http :5000 --wsgi-file wsgi.py --callable app
  - Heroku/Railway: Automatically detects this file
"""

from app import app

# Expose the Flask app as 'application' (standard WSGI callable name)
application = app

if __name__ == "__main__":
    # This is only used when running directly with Python (for testing)
    # In production, use a WSGI server like Gunicorn instead
    app.run(host='0.0.0.0', port=5000, debug=False)
