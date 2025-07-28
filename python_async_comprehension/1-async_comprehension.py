#!/usr/bin/env python3
"""
This module contains a method
in this module
"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    The said method
    in question.
    """
    return [i async for i in async_generator()]
