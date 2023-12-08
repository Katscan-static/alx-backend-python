#!/usr/bin/env python3
"""
    This module typechecks using mypy
"""

from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
        zoom_array:
            this finction zooms into a Tuple

        Args:
            lst (Tuple): A tuple
            factor (int):

        Returns:
            Tuple: zoomed in tuple
    """
    zoomed_in: Tuple = tuple([
        item for item in lst
        for i in range(factor)
    ])
    return list(zoomed_in)


array = tuple([12, 72, 91])

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
