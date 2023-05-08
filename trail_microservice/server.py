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
    query = socket.recv()
    # Using string slicing to find statement type
    print(f"Received query with start: {query[:5]}")
