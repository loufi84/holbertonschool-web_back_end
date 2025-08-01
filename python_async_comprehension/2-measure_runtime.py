#!/usr/bin/env python3
"""
This module contains a method
in this module
"""
import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    The said method
    in question.
    """
    start = time.time()
    await asyncio.gather(*[async_comprehension() for n in range(4)])
    end = time.time()
    return end - start
