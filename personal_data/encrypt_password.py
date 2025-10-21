#!/usr/bin/env python3
"""Module for password encryption using bcrypt"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hashes a password with a random salt using bcrypt.

    Args:
        password: The password string to hash

    Returns:
        A salted, hashed password as a byte string
    """
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password
