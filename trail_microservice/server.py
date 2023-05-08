"""
Created by: Matthew O'Malley-Nichols
Code based off of: https://zeromq.org/languages/python/
"""
import time
import zmq
import create_trails_database
import sqlite3

class REPSocket():
    def __init__(self):
        self.context = zmq.Context()
        # Using REP and REQ socket pair
        self.socket = self.context.socket(zmq.REP)
        self.socket.bind("tcp://*:5555")

DBCONN = sqlite3.connect("trails.db")
CURSOR = DBCONN.cursor()
SOCKET = REPSocket().socket

def main():
    # Creates tables in trails.db if they do not already exist
    create_trails_database.create_tables()

    while True:
       receive_sql_request() 

def receive_sql_request(): 
        query = SOCKET.recv_string()
        # Using string slicing to find statement type
        print(f"Received query with start: {query[:6]}")
        # TODO: refactor out query logic 
        result = "Failure"
        match query[:6]:
            case "SELECT": 
                result = select_statement(query)
            case "DELETE":
                result = delete_or_insert_statement(query)
            case "INSERT":
                result = delete_or_insert_statement(query)
        time.sleep(1)
        SOCKET.send_string(result)

def delete_or_insert_statement(query) -> str:
    try:
        CURSOR.execute(query)
        DBCONN.commit()
        return "Success" 
    except:
        return "Failure"

def select_statement(query):
    CURSOR.execute(query)
    output = CURSOR.fetchall()
    results = ""
    for row in output:
        print(f"{row}")
        results += row
    return results


if __name__ == "__main__":
    main()
