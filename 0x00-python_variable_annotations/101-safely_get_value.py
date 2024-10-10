#!/usr/bin/env python3
"""
101-safely_get_value  :
    2th Advanced Task of the project
"""

from typing import TypeVar, Mapping, Any, Union

T = TypeVar('T')
R = Union[Any, T]
D = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: D = None) -> R:
    """
    element_length  :
    return 1st index if lst exists
    """
    if key in dct:
        return dct[key]
    else:
        return default
