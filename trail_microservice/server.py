"""
Created by: Matthew O'Malley-Nichols
Code based off of: https://zeromq.org/languages/python/
"""
import time
import zmq
import create_trails_database


def main():
    # Creates tables in trails.db if they do not already exist
    create_trails_database.create_tables()
    socket = setup_server()

    while True:
       receive_sql_request(socket) 

def receive_sql_request(socket: zmq.Socket): 
        query = socket.recv_string()
        # Using string slicing to find statement type
        print(f"Received query with start: {query[:6]}")
        # TODO: refactor out query logic 
        match query[:6]:
            case "SELECT": 
                print("DELETE STATEMENT")
            case "DELETE":
                print("DELETE STATEMENT")
            case "INSERT":
                print("INSERT STATEMENT")
            case _:
                print("Nothing matched")
        time.sleep(1)
        socket.send(b"NOT YET IMPLEMENTED")

def setup_server() -> zmq.Socket:
    # Server setup from zeroMQ
    context = zmq.Context()
    # Using REP and REQ socket pair
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")
    return socket


if __name__ == "__main__":
    main()
