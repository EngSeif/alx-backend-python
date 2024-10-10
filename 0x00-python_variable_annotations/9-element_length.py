"""
9-element_length  :
    9th Task of the project
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    element_length  :
    return element and its length in a list
    of tuples
    """
    return [(i, len(i)) for i in lst]
