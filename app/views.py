from app import app
from flask import render_template, request, redirect, url_for, flash
import datetime

###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mopp Head")


def format_date_joined(date):
    return date.strftime("%B, %Y")  # formatted date

@app.route('/profile')
def profile():
    date_joined = datetime.date(2026, 1, 7)
    joined = "Joined " + format_date_joined(date_joined)

    user = {
        "full_name": "Mopp Head",
        "username": "mhead",
        "location": "Calliaqua, St.Vincent and the Grenadines",
        "bio": "I am a young man interested in making the world a better place. This may be through various projects or inventions that can make people's lives easier. I enjoy working with others so reach out if you would like to join me.",
        "posts": 19,
        "following": 306,
        "followers": 578,
        "joined": joined,
        "photo": "man.jpg"
    }

    return render_template('profile.html', user=user)
###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
