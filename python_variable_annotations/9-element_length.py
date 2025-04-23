#!/usr/bin/env python3
"""
9-element_length
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Return a list of tuples where each tuple contains an element
    and its length.
    """
    return [(i, len(i)) for i in lst]
