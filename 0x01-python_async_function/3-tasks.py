#!/usr/bin/env python3
"""
3-tasks.py:
    fourth Task of the project
"""
import asyncio
from asyncio import Task

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """
    task_wait_random   :
    takes an integer max_delay and returns a asyncio.Task
    """
    task: Task = asyncio.create_task(wait_random(max_delay))
    return task
