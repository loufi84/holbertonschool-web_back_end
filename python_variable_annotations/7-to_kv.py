#!/usr/bin/env python3
"""
This module provides a function that returns a tuple with a
string and the square of a number
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
        Takes a string k and an int or float v, returns a tuple with k and
        the square of v
    """
    return (k, v * v)
