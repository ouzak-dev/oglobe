from flask import Flask
from flask_mail import Mail, Message
import secrets

# create the app
app = Flask(__name__)
# add a secret key
app.config["SECRET_KEY"] = secrets.token_hex()
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
