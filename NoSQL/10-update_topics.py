#!/usr/bin/env python3
"""
This module contains a single method that changes all topics of a school
document, based on the name.
"""


def update_topics(mongo_collection, name, topics):
    """
    The method that update the topics.
    Args:
        mongo_collection: The collection to target
        name: The name of the school
        topics: The topics to add
    """
    updated = mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
    return updated
