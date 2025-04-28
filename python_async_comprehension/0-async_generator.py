#!/usr/bin/env python3
"""Module containing an asynchronous generator that yields random numbers."""
import asyncio
import random


async def async_generator():
    """Random number 0 to 10"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
