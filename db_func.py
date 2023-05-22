# Author: Brendan Cook
# Date: 05/05/23
# Description: Defines functions to handle SQL request from the client.


import sqlite3


# Connect to the hash database
connection = sqlite3.connect('hash.db')
cursor = connection.cursor()


def insert_db(sql):
    """Inserts entry into the hash database. 
    Returns True when complete. Takes an SQL
    statement as the only parameter."""
    # Insert data
    try:
        cursor.execute(sql)
        connection.commit()
        return True
    except:
        return "Failure"


def select_db(sql):
    """Selects entry(ies) from the hash database. 
    Returns the entries as text in a new line
    when complete. Takes an SQL statement as the 
    only parameter."""
    # Select data
    try:
        cursor.execute(sql)
        data = cursor.fetchall()
        results = ''

        if len(data) == 0:
            # No entries found
            results = "Not Found"
            return results

        for i in range(len(data)):
            items = data[i]
            for j in range(len(items)):
                values = items[j]
                results = results + values
                if j < (len(items) - 1):
                    results = results + ' '
                if j == (len(items) - 1):
                    results = results + '\n'
        return results
    except:
        return "Failure"


def delete_db(sql):
    """Deletes entry from the hash database. 
    Returns True when complete. Takes an SQL
    statement as the only parameter."""
    cursor.execute(sql)
    connection.commit()
    return True
