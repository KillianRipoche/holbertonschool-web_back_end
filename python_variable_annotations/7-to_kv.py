#!/usr/bin/env python3
"""
7-to_kv
"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Return a tuple composed of a string key and the square of a numeric value
    as float.
    """
    squared: float = float(v * v)
    return (k, squared)
