#!/usr/bin/env python3
"""
This module will provide a single method, returning a tuple of size 2
containing a start index and an end index corresponding to the range of
indexes to return in a list for page and page_size pagination parameters.
"""


def index_range(page, page_size):
    """
    This method will return the tuple for pagination.
    Args:
        page:  The page number to retrieve
        page_size: The number of items per page
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    size = (start_index, end_index)
    return size
