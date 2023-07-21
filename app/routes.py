from flask import render_template, session, request, redirect, url_for, flash, abort
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

@app.route('/contact')
def contact():
    return render_template('contact.html', page="contact")
