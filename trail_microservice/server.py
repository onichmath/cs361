"""
Created by: Matthew O'Malley-Nichols
Code based off of: https://zeromq.org/languages/python/
"""
import time
import zmq
import create_trails_database
import sqlite3

class REPSocket():
    def __init__(self, connection = "tcp://*:5555"):
        self.context = zmq.Context()
        # Using REP and REQ socket pair
        self.socket = self.context.socket(zmq.REP)
        self.socket.bind(connection)

DBCONN = sqlite3.connect("trails.db")
CURSOR = DBCONN.cursor()
SOCKET = REPSocket().socket

def main():
    # Creates tables in trails.db if they do not already exist
    create_trails_database.create_tables()
    flag = True
    while flag:
       flag = receive_sql_request() 

def receive_sql_request(): 
    """
    Matches query from client to cases and returns result to client
    """
    query = SOCKET.recv_string()
    # Using string slicing to find statement type
    print(f"Received query: {query}")
    # TODO: refactor out query logic 
    result = "Failure"
    match query[:6]:
        case "SELECT": 
            result = select_statement(query)
        case "DELETE":
            result = delete_or_insert_statement(query)
        case "INSERT":
            result = delete_or_insert_statement(query)
        case "q":
            return False
    time.sleep(1)
    SOCKET.send_string(result)

def delete_or_insert_statement(query) -> str:
    """
    Executes query and commits it to memory
    :param query: from SOCKET.recv_string() 
    :return: returns either success or failure
    """
    try:
        CURSOR.execute(query)
        DBCONN.commit()
        return "Success" 
    except:
        return "Failure"

def select_statement(query):
    """
    Executes select statement and returns results delimited by pipe operator.
    To parse results, use regex: [^\|]+ to match anything not pipe 1 or more times
    Or simply change delimiter
    :param query: from SOCKET.recv_string() 
    :return: either results or Failure if it fails
    """
    try:
        CURSOR.execute(query)
        output = CURSOR.fetchall()
        
        if len(output) == 0: return "No matches"

        results = ""
        for row in output:
            for column in row:
                results += f"{str(column)}|" 
            results += "\n"

        return results
    except:
        return "Failure"


if __name__ == "__main__":
    main()
