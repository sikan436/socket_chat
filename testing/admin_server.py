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
            m1=message.decode('ascii')
            mn=m1.split(':',1)
            nick=mn[0]
            words=mn[1]
            print (f'message {words} recieved from alias {nick}')
            # print (f'words of msg are {words} ')
            first_char=words[0]
            print (f"first char is {first_char}")
            if nick=='admin' and first_char=='/':
                print('command recieved from admin, taking action')
                culpit=words.split(' ',1)
                name=culpit[1]
                print (f'he is the culpit {name}')
                print (clients)
                print(aliases)
                name.close()
                index=clients.index(name)
                print('before name remove ')
                clients.remove(name)
                print(f'client removed is name {name}')
                client.close()
                print ('client closed')
                alias=aliases[index]
                print ('before broadcast')
                broadcast(f" {alias} banned by admin ".encode('ascii'))
                print('after broadcast')
                aliases.remove(alias)

                continue
            broadcast(message)
        except:
            index=clients.index(client)
            print(f'client removed is {client}')
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
            if password=='admin':
                print ('admin logged in ')

        aliases.append(alias)
        clients.append(client)
        print(f"accepted connection from {alias}")
        broadcast(f"{alias} joined the chat".encode('ascii'))
        client.send("you are now connected".encode('ascii'))
        thread=threading.Thread(target=handle_client,args=(client,))
        thread.start()
if __name__=="__main__":
    run_server()