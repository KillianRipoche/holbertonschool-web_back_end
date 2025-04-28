#!/usr/bin/env python3
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    This is a com
    Random number 0 to 10
    """
    for _ in range(10):  # convention en python pour ne pas définir de valeur
        await asyncio.sleep(1)
        yield random.random() * 10
