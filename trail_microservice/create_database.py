"""
Author: Matthew O'Malley-Nichols
Tables from Brendan Cook
"""

import sqlite3

# TODO: Refactor
def create_trails_table():
    # Attempts to connect to trails.db, else creates empty db
    connection = sqlite3.connect("trails.db")
    # Use cursor object to send SQL commands to database
    cursor = connection.cursor()
    # Execute create statement
    cursor.execute("""CREATE TABLE IF NOT EXISTS trails (
        trail_id int NOT NULL AUTO_INCREMENT,
        name varchar(45) NOT NULL,
        difficulty varchar(45) NOT NULL,
        length int NOT NULL,
        elev int NOT NULL,
        PRIMARY KEY (trail_id),
        UNIQUE (trail_id))
        """)

def create_riden_table():
    # Attempts to connect to trails.db, else creates empty db
    connection = sqlite3.connect("trails.db")
    # Use cursor object to send SQL commands to database
    cursor = connection.cursor()
    # Execute create statement
    cursor.execute("""CREATE TABLE IF NOT EXISTS riden (
        riden_id int NOT NULL AUTO_INCREMENT,
        trail_id int,
        PRIMARY KEY (riden_id),
        FOREIGN KEY (trail_id) REFERENCES trails(trail_id))
        """)
