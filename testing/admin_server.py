import socket,threading
ip_addr='127.0.0.1'
port=12345
server=socket.socket()
aliases=[]
clients=[]
server.bind((ip_addr,port))


def broadcast(message):
    for client in clients:
        
        client.send(message)
        

def handle_client(client):
    while True:
        try:
            message=client.recv(1024)
            
            broadcast(message)
        except:
            index=clients.index(client)
            clients.remove(client)
            client.close()
            alias=aliases[index]
            broadcast(f" {alias} left the chat".encode('ascii'))
            aliases.remove(alias)
            break

def run_server():
    server.listen(0)
    print(f" server Listening on {ip_addr}:{port}")
    while True :
        client,address= server.accept()

        client.send("your nickname?".encode('ascii'))
        alias=client.recv(1024)
        alias=alias.decode('ascii')
        if alias=='admin':
            client.send('pass'.encode('ascii'))
            password=client.recv(1024).decode('ascii')
            if password!='admin':
                client.send('REFUSE'.encode('ascii'))
                client.close()
                continue
        # if alias=='admin':
            
        #     client.send("enter password?".encode('ascii'))
        #     pwd=client.recv(1024).decode('ascii')
        #     print (f" new password is {pwd}")
        #     if pwd!=password:
        #             client.send("Refuse".encode('ascii'))
        #             client.close()
        #             continue         
        
        aliases.append(alias)
        clients.append(client)
        print(f"accepted connection from {alias}")
        broadcast(f"{alias} joined the chat".encode('ascii'))
        client.send("you are now connected".encode('ascii'))
        thread=threading.Thread(target=handle_client,args=(client,))
        thread.start()
if __name__=="__main__":
    run_server()