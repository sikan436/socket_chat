import socket


def run_client():
    # create a socket object
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_ip = "127.0.0.1"  # replace with the server's IP address
    server_port =12345  # replace with the server's port number
    # establish connection with server
    client.connect((server_ip, server_port))

    while True:
        # input message and send it to the server
        msg = input("Enter message: ")
        client.send(msg.encode("utf-8")[:1024])

        # receive message from the server
        response = client.recv(1024)
        response = response.decode("utf-8")

        # if server sent us "closed" in the payload, we break out of the loop and close our socket
        if response.lower() == "closed":
            break

        print(f"Received: {response}")

    # close client socket (connection to the server)
    client.close()
    print("Connection to server closed")

run_client()





# import socket
# from datetime import datetime,timedelta

# ip_addr='127.0.0.1'
# port=8080


# def run_server():
#     client=socket.socket()
#     client.connect((ip_addr,port)   )
#     while True:
#         msg=input("enter message")
#         client.send(msg.encode("utf-8")[:1024])
#         response=client.recv(1024)
#         response=response.decode("utf-8")

#         if response.lower() == "closed":
#             break

#     print (f"recieved response {response}")

#     client.close()
#     print ("connection closed ")
# run_server()