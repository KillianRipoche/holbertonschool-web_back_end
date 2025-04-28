#!/usr/bin/env python3
"""
Async generator producing 10 random floats between 0 and 10,
wating 1 second before each yield.
"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Asynchronously generate 10 random floats between 0 and 10,
    waiting 1 second before yielding each.

    Yields:
        float: Random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
