from flask import render_template, request, redirect, flash, url_for
from app.functions import send_email
from app import app

####################################################################################################
# errorhandler

@app.errorhandler(404)
def not_found(error):
    return render_template('error/404.html'), 404

@app.errorhandler(500)
def internal_error():
    return render_template('error/500.html'), 500

####################################################################################################
# routes

@app.route('/')
def home():
    return render_template('home.html', page="home")

@app.route('/menu')
def menu():
    return render_template('menu.html', page="menu")

@app.route('/about')
def about():
    return render_template('about.html', page="about")

@app.route('/location')
def location():
    return render_template('location.html', page="location")

@app.get('/contact')
def contact():
    return render_template('contact.html', page="contact")

@app.post('/contact')
def submit_message():
    data = request.form
    name = data.get("name", None)
    email = data.get("email", None)
    subject = data.get("subject", "")
    message = data.get("message", None)
    if not name:
        flash("Please put your name", "error")
    elif not email:
        flash("Please put your email", "error")
    elif not message:
        flash("You can't send empty message", "error")
    else:
        if send_email(name, email, subject, message):
            flash("Your message has been sent", "success")
        else:
            flash("Something went wrong,Please try again", "error")
    return redirect(url_for('contact'))
