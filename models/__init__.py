#!/usr/bin/python3
"""scrpt for (Initialize and reload)"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
