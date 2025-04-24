#!/usr/bin/env python3
"""
This module provides an asynchronous coroutine that waits for
a random delay between 0 and max_delay seconds and returns the delay.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay.

    Args:
        max_delay (int): The maximum number of seconds to wait.
                         Must be a non-negative integer. Default is 10.

    Returns:
        float: The actual delay time waited, a float between 0 and max_delay.
    """
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
