#!/usr/bin/env python3
"""
This is a module with a function
"""
from typing import Sequence, Any, Optional


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """
    This is the function in the module
    """
    if lst:
        return lst[0]
    else:
        return None
