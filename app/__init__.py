from flask import Flask
import secrets

# create the app
app = Flask(__name__)
# add a secret key
app.config["SECRET_KEY"] = secrets.token_hex()

from app import routes
