# Author: Brendan Cook
# Date: 05/05/23
# Description: Defines a function to create the hash database.


import sqlite3

def create_db():
    """Creates the hash database and hashes table. Takes no arguments."""
    # Create database
    connection = sqlite3.connect('hash.db')
    cursor = connection.cursor()
    # Create hashes table
    create_command = """CREATE TABLE IF NOT EXISTS
    hashes(hash TEXT, file_name TEXT)"""
    cursor.execute(create_command)
