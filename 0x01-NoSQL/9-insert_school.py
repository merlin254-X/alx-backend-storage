#!/usr/bin/env python3
""" Module for using PyMongo """


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a MongoDB collection based on keyword arguments.
    
    Args:
        mongo_collection: The pymongo collection object.
        **kwargs: Keyword arguments representing the fields for the document.
        
    Returns:
        The _id of the newly inserted document.
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
