#!/usr/bin/env python3
"""
This module contains a single method that inserts a new document
in a collection based on kwargs
"""


def insert_school(mongo_collection, **kwargs):
    """
    The method that insert the document.
    Args:
        mongo_collection: The collection to target
        kwargs: Variable arguments
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
