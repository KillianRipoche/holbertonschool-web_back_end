#!/usr/bin/env python3
"""Module to measure the average execution time of an async function."""

import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measure the average runtime of wait_n.

    Args:
        n (int): Number of times to run wait_random.
        max_delay (int): Max delay passed to each coroutine.

    Returns:
        float: Average execution time per coroutine.
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.time() - start
    return total_time / n
