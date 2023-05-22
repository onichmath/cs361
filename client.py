import zmq

def client(sql_request):
    context = zmq.Context()
    #  Socket to talk to server
    print("Connecting to hash server…")
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")
    if sql_request == 'exit':
        socket.send(sql_request.encode())
        return
    else:
        socket.send(sql_request.encode())
        #  Get the reply.
        message = socket.recv()
        print(message.decode())
