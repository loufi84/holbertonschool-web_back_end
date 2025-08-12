#!/usr/bin/env python3
"""
This module contains a script that returns all students sorted by average
score.
"""


def top_students(mongo_collection):
    """
    The method that find and sort students.
    Args:
        mongo_collection: The collection to check
    """
    pipeline = [
        {
            "$addFields": {
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {
            "$sort": {"averageScore": -1}
        }
    ]
    return list(mongo_collection.aggregate(pipeline))
