#!/usr/bin/env python3
"""
1-concurrent_coroutines.py:
    Second Task of the project
"""
import asyncio
import random
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    wait_n  :
    will spawn wait_random n times with the specified max_delay.
    """
    wait_time: float = random.uniform(0, max_delay)
    tasks = [asyncio.create_task(wait_random(wait_time)) for _ in range(n)]
    delays = []
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    return delays
