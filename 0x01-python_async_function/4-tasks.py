#!/usr/bin/env python3
"""
1-concurrent_coroutines.py:
    Second Task of the project
"""
import asyncio
import random
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    wait_n  :
    will spawn wait_random n times with the specified max_delay.
    """
    tsks = [task_wait_random(max_delay) for _ in range(n)]
    delays = []
    for task in asyncio.as_completed(tsks):
        delay = await task
        delays.append(delay)
    return delays
