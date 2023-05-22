"""
Created by: Matthew O'Malley-Nichols
Code based off of: https://zeromq.org/languages/python/
"""

import zmq
import time

class REQSocket():
    def __init__(self, connection = "tcp://localhost:5555"):
        self.context = zmq.Context()
        # Using REQ and REP socket pair
        self.socket = self.context.socket(zmq.REQ)
        self.socket.connect(connection)

SOCKET = REQSocket().socket

def main():
    flag = True
    while flag:
        flag = send_sql_request()

def send_sql_request():
    """
    Sends queries to server and prints return message
    """
    # Send requests to db
    request = input("Send a SQL request to server: ")

    # Unicode not allowed
    SOCKET.send_string(request)
    if request == "q": return False

    return_message = SOCKET.recv_string()
    time.sleep(3)
    print(f"Returned: {return_message}")

    return True

if __name__ == "__main__":
    main()
