#!/usr/bin/env python3
"""
2-measure_runtime.py:
    third Task of the project
"""
import time
import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    measure_time  :
    measures the total execution time for wait_n(n, max_delay).
    """
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.time()
    return end_time - start_time
