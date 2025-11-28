#!/usr/bin/env python3
"""
Basic Flask application module.
This module sets up a simple Flask app with a single route.
"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index() -> str:
    """
    Render the index page.

    Returns:
        str: The rendered HTML template for the index page.
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
