from app import app, MAIL, Message

def send_email(name, email, subject, message):
    try:
        # send data to contact mail    
        msg = Message()
        msg.sender = f"{name} <{app.config['MAIL_USERNAME']}>"
        msg.reply_to = email
        msg.recipients = [app.config['MAIL_CONTACT']]
        msg.subject = f"New message :: {subject}"
        msg.body = f'Name:\n        {name}\n\nEmail:\n        {email}\n\nSubject:\n        {subject}\n\nMessage:\n        {message}'
        MAIL.send(msg)
        return True
    except:
        return False
    
    