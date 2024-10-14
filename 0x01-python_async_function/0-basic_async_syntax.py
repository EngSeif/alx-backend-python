#!/usr/bin/env python3
import asyncio
import random

"""
0-basic_async_syntax.py:
    first Task of the project
"""


async def wait_random(max_delay: int = 10) -> float:
    """
    wait_random :
    waits for a random delay between 0 and max_delay
    """
    wait_time = random.uniform(0, max_delay)
    await asyncio.sleep(max_delay)
    return wait_time
