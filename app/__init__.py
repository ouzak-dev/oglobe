from flask import Flask
from flask_mail import Mail, Message
import secrets
import os

# create the app
app = Flask(__name__)

# SECRET_KEY configuration
# In production, set the SECRET_KEY environment variable
# For development, a random key is generated (but will change on restart)
app.config["SECRET_KEY"] = os.environ.get('SECRET_KEY') or secrets.token_hex(32)
# contact mail
app.config['MAIL_CONTACT'] = "contact@oglobe.ma"
# Mail credentials
app.config['MAIL_SERVER'] = "mail.privateemail.com"
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = "auto@example.com"
app.config['MAIL_PASSWORD'] = "Password@example"
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
MAIL = Mail(app)

from app import routes
