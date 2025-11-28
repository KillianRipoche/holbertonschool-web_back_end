#!/usr/bin/env python3
"""
Flask application with user preferred locale support.
This module uses user's preferred locale from their settings.
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel


class Config:
    """
    Configuration class for Flask app.
    Sets up available languages, default locale and timezone.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel()

# Mock user database
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> dict:
    """
    Get user from mock database based on login_as URL parameter.

    Returns:
        dict: User dictionary if found, None otherwise.
    """
    try:
        user_id = request.args.get('login_as')
        if user_id:
            return users.get(int(user_id))
    except (ValueError, TypeError):
        return None
    return None


@app.before_request
def before_request() -> None:
    """
    Execute before all other functions.
    Finds and sets the current user in flask.g.user.
    """
    g.user = get_user()


def get_locale() -> str:
    """
    Determine the best match for supported languages.

    Priority order:
    1. Locale from URL parameters (if valid)
    2. Locale from user settings (if user logged in and locale is valid)
    3. Locale from request header (Accept-Language)
    4. Default locale

    Returns:
        str: The best matching language code (e.g., 'en' or 'fr').
    """
    # 1. Check if locale parameter is in URL
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale

    # 2. Check if user is logged in and has a preferred locale
    if g.user and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user.get('locale')

    # 3. Use the best match from Accept-Language header
    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel.init_app(app, locale_selector=get_locale)


@app.route('/')
def index() -> str:
    """
    Render the index page.

    Returns:
        str: The rendered HTML template for the index page.
    """
    return render_template('6-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
