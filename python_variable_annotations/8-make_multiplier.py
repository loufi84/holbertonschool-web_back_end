#!/usr/bin/env python3
"""
This module provides a method in a method to multiply
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    The method that call the method to multiply
    """
    def multiplier_func(x: float) -> float:
        """
        The method that multiply
        """
        return x * multiplier
    return multiplier_func
