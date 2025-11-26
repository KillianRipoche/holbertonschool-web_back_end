#!/usr/bin/env python3
"""Auth module
"""
import bcrypt
import uuid
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """Hash a password with bcrypt

    Args:
        password: The password string to hash

    Returns:
        bytes: The salted hash of the password
    """
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed


def _generate_uuid() -> str:
    """Generate a new UUID

    Returns:
        str: String representation of a new UUID
    """
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register a new user

        Args:
            email: User's email address
            password: User's password in plain text

        Returns:
            User: The newly created User object

        Raises:
            ValueError: If a user with this email already exists
        """
        try:
            # Check if user already exists
            self._db.find_user_by(email=email)
            # If we reach here, user exists
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            # User doesn't exist, we can create it
            hashed_password = _hash_password(password)
            new_user = self._db.add_user(
                email, hashed_password.decode('utf-8'))
            return new_user

    def valid_login(self, email: str, password: str) -> bool:
        """Validate user login credentials

        Args:
            email: User's email address
            password: User's password in plain text

        Returns:
            bool: True if credentials are valid, False otherwise
        """
        try:
            user = self._db.find_user_by(email=email)
            # Check if password matches
            return bcrypt.checkpw(
                password.encode('utf-8'),
                user.hashed_password.encode('utf-8')
            )
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """Create a session for a user

        Args:
            email: User's email address

        Returns:
            str: The session ID, or None if user not found
        """
        try:
            user = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            self._db.update_user(user.id, session_id=session_id)
            return session_id
        except NoResultFound:
            return None
