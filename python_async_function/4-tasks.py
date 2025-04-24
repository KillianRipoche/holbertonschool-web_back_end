#!/usr/bin/env python3
"""Module that runs task_wait_random concurrently and collects results."""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn task_wait_random n times and return the delays in ascending order.

    Args:
        n (int): Number of concurrent tasks to run.
        max_delay (int): Maximum delay for each task.

    Returns:
        List[float]: Sorted list of delays.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    results: List[float] = []
    for task in asyncio.as_completed(tasks):
        result = await task
        results.append(result)
    return results
