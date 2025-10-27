#!/usr/bin/env python3
"""
Auth module for API authentication
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """
    Auth class to manage API authentication
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines if authentication is required for a given path
        Args:
            path: the path to check
            excluded_paths: list of paths that don't require authentication
        Returns:
            True if authentication is required, False otherwise
        """
        if path is None:
            return True

        if excluded_paths is None or len(excluded_paths) == 0:
            return True

        normalized_path = path if path.endswith('/') else path + '/'

        if normalized_path in excluded_paths:
            return False

        return True

    def authorization_header(self, request=None) -> str:
        """
        Gets the authorization header from the request
        Args:
            request: Flask request object
        Returns:
            None if request is None or Authorization header is missing,
            otherwise returns the value of Authorization header
        """
        if request is None:
            return None

        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Gets the current user from the request
        Args:
            request: Flask request object
        Returns:
            None for now (will be implemented later)
        """
        return None
