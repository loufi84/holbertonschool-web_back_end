#!/usr/bin/env python3
"""
This module provides a method that returns the sum of floats or integers
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    This method returns the sum of all elements of the list input_list
    """
    return sum(mxd_lst)
