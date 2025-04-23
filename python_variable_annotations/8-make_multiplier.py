#!/usr/bin/env python3
"""
8-make_multiplier
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Return a function that multiplies a float by the given multiplier.
    """
    def multiplier_fn(x: float) -> float:
        """Multiply x by the captured multiplier."""
        return multiplier * x

    return multiplier_fn
