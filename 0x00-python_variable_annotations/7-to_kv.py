#!/usr/bin/python3
"""
    this module returns a tuple of a string and number (float or int)
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
        to_kv:
            returns a key, value tuple

        Args:
            k (str): key value which is a string
            v (Union[int, float]): value which is an int or float

        Returns:
            Tuple[str, float]
    """

    return k, v ** 2
