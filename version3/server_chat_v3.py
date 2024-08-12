import socket

ip_address='127.0.0.1'
port=12345

def run_server():
    server=socket.socket()
    server.bind((ip_address,port))
    # listen for incoming connections
    server.listen(0)
    print(f"Listening on {ip_address}:{port}")
    # accept incoming connections
    client_socket, client_address = server.accept()
    print(f"Accepted connection from {client_address[0]}:{client_address[1]}")

    # receive data from the client
    while True:
        request = client_socket.recv(1024)
        request = request.decode("utf-8") # convert bytes to string
        input=("hi there")
        client_socket.send(f"{input}".encode()) 
        
        # if we receive "close" from the client, then we break
        # out of the loop and close the conneciton
        if request.lower() == "close":
            # send response to the client which acknowledges that the
            # connection should be closed and break out of the loop
            client_socket.send("closed".encode("utf-8"))
            break

        print(f"Received: {request}")

        response = "accepted".encode("utf-8") # convert string to bytes
        # convert and send accept response to the client
        client_socket.send(response)

        # close connection socket with the client
    client_socket.close()
    print("Connection to client closed")
        # close server socket
    server.close()
run_server()






