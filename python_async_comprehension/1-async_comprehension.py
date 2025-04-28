#!/usr/bin/env python3
"""
Collect 10 random floats using async comprehensions.
"""
from typing import List

# Dynamic import of the async_generator from file 0-async_generator.py
async_generator = __import__('0-async_generator').async_generator

async def async_comprehension() -> List[float]:
    """
    Return a list with async generator
    """
    return [number async for number in async_generator()]
