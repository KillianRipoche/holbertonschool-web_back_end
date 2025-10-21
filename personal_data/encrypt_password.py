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


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Validates that the provided password matches the hashed password.

    Args:
        hashed_password: The hashed password as bytes
        password: The plain text password to verify

    Returns:
        True if the password matches the hash, False otherwise
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
