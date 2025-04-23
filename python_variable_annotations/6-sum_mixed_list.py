#!/usr/bin/env python3
"""
6-sum_mixed_list
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Return the sum of a list containing both ints and floats.
    """
    total: float = sum(mxd_lst)
    return total
