#!/usr/bin/env python3
"""
7-kv  :
    8th Task of the project
"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[Union[str, float]]:
    """
    to_kv  :
    that takes a string k and
    an int OR float v as arguments
    and returns a tuple.
    """
    return (k, float(v ** 2))
