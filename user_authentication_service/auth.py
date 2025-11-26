#!/usr/bin/env python3
"""Auth module
"""
import bcrypt
import uuid
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
from typing import Union


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

    def get_user_from_session_id(self, session_id: str) -> Union[User, None]:
        """Get user from session ID

        Args:
            session_id: The session ID string

        Returns:
            User: The corresponding user, or None if not found
        """
        if session_id is None:
            return None

        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """Destroy a user's session

        Args:
            user_id: The user's ID

        Returns:
            None
        """
        self._db.update_user(user_id, session_id=None)

    def get_reset_password_token(self, email: str) -> str:
        """Generate a reset password token for a user

        Args:
            email: User's email address

        Returns:
            str: The reset token

        Raises:
            ValueError: If user does not exist
        """
        try:
            user = self._db.find_user_by(email=email)
            reset_token = _generate_uuid()
            self._db.update_user(user.id, reset_token=reset_token)
            return reset_token
        except NoResultFound:
            raise ValueError

    def update_password(self, reset_token: str, password: str) -> None:
        """Update user's password using reset token

        Args:
            reset_token: The reset token
            password: The new password in plain text

        Returns:
            None

        Raises:
            ValueError: If reset token is invalid
        """
        try:
            user = self._db.find_user_by(reset_token=reset_token)
            hashed_password = _hash_password(password)
            self._db.update_user(
                user.id,
                hashed_password=hashed_password.decode('utf-8'),
                reset_token=None
            )
        except NoResultFound:
            raise ValueError
