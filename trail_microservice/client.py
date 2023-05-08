"""
Created by: Matthew O'Malley-Nichols
Code based off of: https://zeromq.org/languages/python/
"""

import zmq

context = zmq.Context()
print("Connecting to server")
# Using REQ and REP socket pair
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

while True:
    # Send requests to db
    # TODO: SQLless queries
    request = input("Send a SQL request to server: ")
    socket.send(request)

    return_message = socket.recv()
    print(f"Returned: {return_message}")