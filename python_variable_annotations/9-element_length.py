#!/usr/bin/env python3
"""
This module provides a method that return a list of tuples each containing
every element and its length
"""
from typing import Tuple, Sequence, Iterable, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    This method take an iterable of sequences and returns a list of tuples with
    each sequence and its length
    """
    return [(i, len(i)) for i in lst]
