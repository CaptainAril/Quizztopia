#!/usr/bin/python3
"""Initializes the model package."""

from models.db_storage import DBStorage

storage = DBStorage()
storage.reload()