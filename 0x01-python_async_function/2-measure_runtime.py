#!/usr/bin/env python3
"""
2-measure_runtime.py:
    third Task of the project
"""
import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    measure_time  :
    measures the total execution time for wait_n(n, max_delay).
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    final_time = (end_time - start_time) / n
    return final_time
