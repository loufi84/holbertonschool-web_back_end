#!/usr/bin/env python3
"""
This is a module with a function
"""
from typing import Mapping, Any, Union, TypeVar


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
    This is the said function
    """
    if key in dct:
        return dct[key]
    else:
        return default
