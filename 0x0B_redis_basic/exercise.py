#!/usr/bin/env python3
"""
Module for Redis cache operations
"""
import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    Decorator that counts how many times a method is called

    Args:
        method: The method to be decorated

    Returns:
        Callable: The wrapped method that increments a counter
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Wrapper function that increments the call counter

        Args:
            self: The instance of the class
            *args: Positional arguments
            **kwargs: Keyword arguments

        Returns:
            The return value of the original method
        """
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    Decorator that stores the history of inputs and outputs for a function

    Args:
        method: The method to be decorated

    Returns:
        Callable: The wrapped method that logs inputs and outputs
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Wrapper function that stores inputs and outputs in Redis lists

        Args:
            self: The instance of the class
            *args: Positional arguments
            **kwargs: Keyword arguments

        Returns:
            The return value of the original method
        """
        # Create keys for inputs and outputs lists
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"

        # Store input arguments as string
        self._redis.rpush(input_key, str(args))

        # Execute the original method
        output = method(self, *args, **kwargs)

        # Store output
        self._redis.rpush(output_key, output)

        return output
    return wrapper


def replay(method: Callable) -> None:
    """
    Display the history of calls of a particular function

    Args:
        method: The method whose history to display
    """
    # Get Redis instance from the method's self (first call will have it)
    # We need to access the Redis instance through the method
    redis_instance = redis.Redis()

    # Get the qualified name
    method_name = method.__qualname__

    # Create keys for inputs and outputs
    input_key = f"{method_name}:inputs"
    output_key = f"{method_name}:outputs"

    # Get all inputs and outputs using LRANGE
    inputs = redis_instance.lrange(input_key, 0, -1)
    outputs = redis_instance.lrange(output_key, 0, -1)

    # Display the number of calls
    call_count = len(inputs)
    print(f"{method_name} was called {call_count} times:")

    # Use zip to iterate over inputs and outputs together
    for input_data, output_data in zip(inputs, outputs):
        # Decode bytes to string for display
        input_str = input_data.decode('utf-8')
        output_str = output_data.decode('utf-8')

        # Display in the required format
        print(f"{method_name}(*{input_str}) -> {output_str}")


class Cache:
    """
    Cache class for storing data in Redis
    """

    def __init__(self):
        """
        Initialize Redis client and flush the database
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in Redis with a random key

        Args:
            data: The data to store (can be str, bytes, int, or float)

        Returns:
            str: The randomly generated key used to store the data
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[
            str, bytes, int, float, None]:
        """
        Retrieve data from Redis and optionally convert it

        Args:
            key: The key to retrieve
            fn: Optional callable to convert the data back to desired format

        Returns:
            The data in the original format if fn is provided, otherwise bytes
            Returns None if key doesn't exist
        """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """
        Retrieve data from Redis and convert it to UTF-8 string

        Args:
            key: The key to retrieve

        Returns:
            str: The data as a UTF-8 string
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """
        Retrieve data from Redis and convert it to integer

        Args:
            key: The key to retrieve

        Returns:
            int: The data as an integer
        """
        return self.get(key, fn=int)
