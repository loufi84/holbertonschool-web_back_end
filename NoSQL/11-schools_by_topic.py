#!/usr/bin/env python3
"""
This module provides a single method that returns the list of schools
having a specificntopic.
"""


def schools_by_topic(mongo_collection, topic):
    """
    The method returning the list.
    Args:
        mongo_collection: The collection to target.
        topic: The topic to search
    """
    return list(mongo_collection.find({"topics": topic}))
