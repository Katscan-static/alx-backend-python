#!/usr/bin/env python3
"""
    this module returns a function that multiplies a float
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
        make_multiplier:
            generates a function that multiplies a float

        Args:
            multiplier (float): The value to be used in the function

        Returns:
            Callable[[float], float]: Returns a function to multiply
    """

    def mult_func(n: float) -> float:
        """
            mult_func:
                returns a value multiplied by (multiplier)

            Args:
                n (float): number to be used to multiply

            Returns:
                float: the multiplied value
        """

        return n * multiplier

    return mult_func
