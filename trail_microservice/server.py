"""
Created by: Matthew O'Malley-Nichols
Code based off of: https://zeromq.org/languages/python/
"""
import time
import zmq
import create_trails_database

# Creates tables in trails.db if they do not already exist
create_trails_database.create_tables()

# Server setup from zeroMQ
context = zmq.Context()
# Using REP and REQ socket pair
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    query = socket.recv_string()
    # Using string slicing to find statement type
    print(f"Received query with start: {query[:6]}")
    # TODO: Query database
    match query[:6]:
        case "SELECT":
            print("SELECT STATEMENT")
        case "DELETE":
            print("DELETE STATEMENT")
        case "INSERT":
            print("INSERT STATEMENT")
        case _:
            print("Nothing matched")
    time.sleep(1)
    socket.send(b"NOT YET IMPLEMENTED")
