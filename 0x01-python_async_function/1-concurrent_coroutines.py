#!/usr/bin/env python3
import asyncio
import random

"""
1-concurrent_coroutines.py:
    Second Task of the project
"""

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> float:
    """
    wait_n  :
    will spawn wait_random n times with the specified max_delay.
    """
    wait_time: float = random.uniform(0, max_delay)
    R = await asyncio.gather(*(wait_random(wait_time) for i in range(0, n)))
    return R
