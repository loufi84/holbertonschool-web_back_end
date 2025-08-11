#!/usr/bin/env python3
"""
This module will provide a single method, returning a tuple of size 2
containing a start index and an end index corresponding to the range of
indexes to return in a list for page and page_size pagination parameters.
"""
import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        start, end = index_range(page, page_size)
        data = self.dataset()
        return data[start:end]

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
