"""
Created by: Matthew O'Malley-Nichols
Code based off of: https://zeromq.org/languages/python/
"""

import zmq


def main():
    socket = setup_client()
    while True:
        send_sql_request(socket)

def send_sql_request(socket: zmq.Socket):
    # Send requests to db
    request = input("Send a SQL request to server: ")
    # Unicode not allowed
    socket.send_string(request)
    return_message = socket.recv()
    print(f"Returned: {return_message}")

def setup_client() -> zmq.Socket:
    context = zmq.Context()
    print("Connecting to server")
    # Using REQ and REP socket pair
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")
    return socket

if __name__ == "__main__":
    main()
