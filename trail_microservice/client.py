"""
Created by: Matthew O'Malley-Nichols
Code based off of: https://zeromq.org/languages/python/
"""

import zmq


class REQSocket():
    def __init__(self):
        self.context = zmq.Context()
        # Using REQ and REP socket pair
        self.socket = self.context.socket(zmq.REQ)
        self.socket.connect("tcp://localhost:5555")

SOCKET = REQSocket().socket

def main():
    while True:
        send_sql_request()

def send_sql_request():
    # Send requests to db
    request = input("Send a SQL request to server: ")
    # Unicode not allowed
    SOCKET.send_string(request)
    return_message = SOCKET.recv_string()
    print(f"Returned: {return_message}")

if __name__ == "__main__":
    main()
