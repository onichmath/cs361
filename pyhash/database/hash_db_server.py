# Author: Brendan Cook
# Date: 05/05/23


import zmq
import db_func
import hash_database

"""Script to set up and run microservices. This script creates a database by calling the 
create_db function from the hash_database.py file. Creates a socket using ZeroMQ module. 
Listens fro request from the client. Processes the request and calls the correct function
to handle the SQL request from the db_func.py file."""

# Create database
hash_database.create_db()

# Set up server
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")


while True:
    #  Wait for next request from client
    sql = socket.recv()
    print("Received request: ", sql.decode())

    if 'INSERT' in sql.decode():
        # Calls insert function to add to entry to the database
        results = db_func.insert_db(sql.decode())
        if results is True:
            socket.send(b'Success')

    elif 'SELECT' in sql.decode():
        # Calls select function to return results of a request
        results = db_func.select_db(sql.decode())
        socket.send(results.encode())

    elif 'DELETE' in sql.decode():
        # Calls delete function to remove entry from database
        results = db_func.delete_db(sql.decode())
        if results is True:
            socket.send(b'Success')

    elif sql.decode() == 'exit':
        # Closes the connection and ends the script
        break
















