#!/usr/bin/env python3
"""Coroutine called async_generator that takes no arguments."""


import asyncio
import random
import typing


async def async_generator() -> typing.Generator[float, None, None]:
    """
    The coroutine will loop 10 times
    """

    for _ in range(0, 10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
