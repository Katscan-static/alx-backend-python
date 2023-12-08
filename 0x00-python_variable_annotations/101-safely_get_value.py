#!/usr/bin/env python3
"""
    this mode safely gets a value
"""

from typing import Any, Mapping as MP, Union as UN, TypeVar
T = TypeVar('T')


def safely_get_value(dct: MP, key: Any, default: UN[T, None]) -> UN[Any, T]:
    """
        safely_get_value:
            safely gets a value

        Args:
            dct (Mapping): A dictionary value
            key (Any): a key of any value
            default (None): None default value
    """
    if key in dct:
        return dct[key]
    else:
        return default
