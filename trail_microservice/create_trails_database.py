"""
Author: Matthew O'Malley-Nichols
Tables from Brendan Cook
"""

import sqlite3

def create_tables():
    """Main connects to trails.db and executes create statements using a cursor object"""
    # Attempts to connect to trails.db, else creates empty db
    connection = sqlite3.connect("trails.db")
    # Use cursor object to send SQL commands to database
    cursor = connection.cursor()
    # Execute both create statements
    create_trails_table(cursor)
    create_riden_table(cursor)

def create_trails_table(cursor: sqlite3.Cursor):
    """Create trails table executes a create table statement on a SQL cursor object""" 
    # Execute create statement
    cursor.execute("""CREATE TABLE IF NOT EXISTS trails (
        trail_id int NOT NULL,
        name varchar(45) NOT NULL,
        difficulty varchar(45) NOT NULL,
        length int NOT NULL,
        elev int NOT NULL,
        PRIMARY KEY (trail_id),
        UNIQUE (trail_id))
        """)

def create_riden_table(cursor: sqlite3.Cursor):
    """Create riden table executes a create table statement on a SQL cursor object""" 
    # Execute create statement
    cursor.execute("""CREATE TABLE IF NOT EXISTS riden (
        riden_id int NOT NULL,
        trail_id int,
        PRIMARY KEY (riden_id),
        FOREIGN KEY (trail_id) REFERENCES trails(trail_id))
        """)

if __name__ == "__main__":
    create_tables()
