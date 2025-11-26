#!/usr/bin/env python3
"""Setup basic Flask
"""
from flask import Flask, jsonify, request, abort, make_response, redirect
from auth import Auth


app = Flask(__name__)
AUTH = Auth()


@app.route("/", strict_slashes=False)
def welcome():
    """Display a welcome message
    """
    return jsonify({"message": "Bienvenue"}), 200


@app.route("/users", methods=["POST"], strict_slashes=False)
def users() -> str:
    """ POST /users/
    JSON body:
      - email
      - password
    Return:
      - User object JSON represented
      - 400 if can't create the new User
    """
    email = request.form.get('email')
    pwd = request.form.get('password')

    if not email or not pwd:
        return jsonify({"message": "email and password are required"}), 400

    try:
        user = AUTH.register_user(email, pwd)
        return jsonify({"email": user.email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route("/sessions", methods=["POST"], strict_slashes=False)
def login() -> str:
    """ POST /sessions/
    JSON body:
      - email
      - password
    Returns:
      - User object JSON represented
      - abort with 401 status
    """
    email = request.form.get('email')
    pwd = request.form.get('password')

    if not email or not pwd:
        abort(401)

    if not AUTH.valid_login(email, pwd):
        abort(401)

    session_id = AUTH.create_session(email)
    response = make_response(jsonify({"email": email, "message": "logged in"}))
    response.set_cookie("session_id", session_id)

    return response


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout_user() -> str:
    """ DELETE /sessions/
    Removes the user session
    """
    session_id = request.cookies.get('session_id')

    if session_id is None:
        abort(403)

    user = AUTH.get_user_from_session_id(session_id)

    if user is None:
        abort(403)

    AUTH.destroy_session(user.id)

    response = make_response(redirect('/'))
    response.delete_cookie('session_id')
    return response


@app.route('/profile', strict_slashes=False)
def find_user():
    """ GET /profile/
    JSON body:
      - session_id
    Return:
      - A JSON payload status code 200
    """
    session_id = request.cookies.get('session_id')
    if session_id is None:
        abort(403)

    user = AUTH.get_user_from_session_id(session_id)
    if user is None:
        abort(403)

    return jsonify({"email": user.email}), 200


@app.route('/reset_password', methods=["POST"], strict_slashes=False)
def get_reset_password_token():
    """ POST /reset_password/
    JSON body:
        email
    Returns:
        JSON payload (email, token) of the user
        abort 403 if the email is not registered
    """
    email = request.form.get('email')
    if email is None:
        abort(401)

    try:
        token = AUTH.get_reset_password_token(email=email)
        return jsonify({"email": email, "reset_token": token})

    except ValueError:
        abort(403)


@app.route('/reset_password', methods=["PUT"], strict_slashes=False)
def update_password():
    """ PUT /reset_password
    JSON body:
        email
        reset_token
        new_password
    Returns:
        JSON payload and status code 200
        abort 403 if the token is invalid
    """
    email = request.form.get('email')
    reset_token = request.form.get('reset_token')
    new_password = request.form.get('new_password')
    if email is None or reset_token is None or new_password is None:
        abort(401)

    try:
        AUTH.update_password(reset_token, new_password)
        return jsonify({"email": email, "message": "Password updated"})

    except ValueError:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
