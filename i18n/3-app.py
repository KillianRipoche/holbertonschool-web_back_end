#!/usr/bin/env python3
"""
A simple flask app
"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """
    Configuration class for the Flask app
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)


def get_locale():
    """
    Get the locale from the request
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel.init_app(app, locale_selector=get_locale)


@app.route('/')
def hello_world():
    """
    Render the 3-index.html template
    """
    return render_template('3-index.html')
