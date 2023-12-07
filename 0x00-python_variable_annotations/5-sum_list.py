#!/usr/bin/python3
"""
    - This module adds float numbers in a list and returns the value
"""
from typing import List

def sum_list(input_list: List[float]) -> float:
    """
        sum_list:
            adds float numbers in a list

        Args:
            input_list (list[float]): a list of float numbers

        Returns:
            float: sum of all floats in the list
    """

    return sum(input_list)
