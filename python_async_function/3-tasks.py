#!/usr/bin/env python3
"""
This module provides a function that creates and returns
an asyncio.Task for the wait_random coroutine.
"""

import asyncio
from typing import Any
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Return an asyncio.Task that runs wait_random with max_delay.

    Args:
        max_delay (int): Maximum delay to pass to wait_random.

    Returns:
        asyncio.Task: The created asyncio Task object.
    """
    return asyncio.create_task(wait_random(max_delay))
