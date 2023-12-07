#!/usr/bin/python3
"""
    - This module returns a sum of mixed values of type int and float
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
        sum_mixed_list:
            sums the float and int type values in a list

        Args:
            mxd_lst (List(Union[int, float])): list of floats and ints

        Returns:
            List[Union[int, float]]: sum of all elements in an array
    """

    return sum(mxd_lst)
