#!/usr/bin/env python3
"""
A module that provides a method
"""
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List(float):
    """
    The method
    """
    return [i async for i in async_generator()]
