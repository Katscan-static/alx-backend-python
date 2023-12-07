#!/usr/bin/env python3
"""
    This module returns length of a list
"""

from typing import Iterable, Tuple, Sequence, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
        element_length:
            returns length of the lst

        Args:
            lst (Iterable[Sequence]): Iterable sequence

        Returns:
            List[Tuple[Sequence, int]]: returns a list of tuple
    """
    return [(i, len(i)) for i in lst]
