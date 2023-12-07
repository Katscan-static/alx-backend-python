#!/usr/bin/env python3
"""
    use duck typing
"""

from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
        safe_first_element:
            return the first element

        Args:
            lst (Sequence[Any]: sequence of any data

        Returns:
            Union[Any, None]: returns any data or None
    """
    if lst:
        return lst[0]
    else:
        return None
