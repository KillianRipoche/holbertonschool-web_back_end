#!/usr/bin/env python3
""" App module
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel
import pytz


class Config():
    """ Config class
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@app.before_request
def before_request():
    """ Before request
    """
    g.user = get_user()


def get_user():
    """ Find user
    """
    user_id = request.args.get('login_as')
    if user_id is not None and user_id.isdigit():
        user_id = int(user_id)
        if user_id in users:
            return users[user_id]

    return None


def get_locale():
    """Determine the best match locale following priority:
    1. Locale from URL parameters
    2. Locale from user settings
    3. Locale from request header
    4. Default locale
    """
    supported_locales = app.config['LANGUAGES']

    url_locale = request.args.get('locale')
    if url_locale in supported_locales:
        return url_locale

    if g.user:
        user_locale = g.user.get('locale')
        if user_locale in supported_locales:
            return user_locale

    header_locale = request.accept_languages.best_match(supported_locales)
    if header_locale:
        return header_locale

    return app.config.get('BABEL_DEFAULT_LOCALE', 'en')


def get_timezone():
    """Determine the best match timezone following priority:
    1. Timezone from URL parameters
    2. Timezone from user settings
    3. Default timezone
    """
    url_timezone = request.args.get('timezone')
    if url_timezone:
        try:
            pytz.timezone(url_timezone)
            return url_timezone
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    if g.user:
        user_timezone = g.user.get('timezone')
        if user_timezone:
            try:
                pytz.timezone(user_timezone)
                return user_timezone
            except pytz.exceptions.UnknownTimeZoneError:
                pass

    return app.config.get('BABEL_DEFAULT_TIMEZONE', 'UTC')


babel = Babel(app, locale_selector=get_locale, timezone_selector=get_timezone)


@app.route('/', strict_slashes=False)
def welcome():
    """ return index
    """
    return render_template("6-index.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5500)
