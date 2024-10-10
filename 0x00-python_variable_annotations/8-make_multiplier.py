#!/usr/bin/env python3
"""
8-make_multiplier  :
    9th Task of the project
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    make_multiplier  :
    that takes a float multiplier as argument and returns a
    function that multiplies a float by multiplier.
    """
    def func(multiplier2: float):
        """
        func  :
        function that multiplies a float by multiplier.
        """
        return multiplier * multiplier2
    return func
