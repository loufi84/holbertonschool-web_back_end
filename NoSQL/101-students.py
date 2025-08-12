#!/usr/bin/env python3
"""
This module contains a script that returns all students sorted by average
score.
"""
import pymongo


def top_students(mongo_collection):
    """
    The method that find and sort students.
    Args:
        mongo_collection: The collection to check
    """
    return mongo_collection.find().sort([("averageScore", pymongo.DESCENDING)])
