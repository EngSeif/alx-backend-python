#!/usr/bin/env python3
"""
100-safe_first_element  :
    1th Advanced Task of the project
"""

from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    element_length  :
    return 1st index if lst exists
    """
    if lst:
        return lst[0]
    else:
        return None
