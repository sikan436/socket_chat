import socket,threading,sys
ip_addr='127.0.0.1'
port=12345
server=socket.socket()
alias=input("enter your alias")
server.connect((ip_addr,port))
if alias=='admin':
    password=input('enter admin password')

stop_thread=False

def msg_rcv():
    while True:
        global stop_thread
        if stop_thread:
            break
        try:
            msg=server.recv(1024).decode('ascii')  #alias

            if msg=='your nickname?':
                server.send(alias.encode('ascii'))
                next_message=server.recv(1024).decode('ascii')
                if next_message=='pass':
                    server.send(password.encode('ascii'))
                    if server.recv(1024).decode('ascii')=='REFUSE':
                        print("connection was refused, wrong pwd")
                        stop_thread=True
                        
            else:
                print(msg)
        except:
            print("error")
            server.close()
            break

def msg_send():
    
    while True:
        if stop_thread:
            break
        try:
            msg=f'{alias}:{input("")}'
            mn=msg.split(':',1)
            words=mn[1]
            # print (f'words of msg are {words}')
            first_char=words[0]
            # print (f"first char is {first_char} " )
            if first_char=='/' and alias!='admin' :
                print ("only admin can fire commands")
                continue
    
            # server.send(msg)
            server.send(msg.encode('ascii'))
        except:
            print ("connection lost")
            server.close()
            break

if __name__=='__main__':
    rcv_thread=threading.Thread(target=msg_rcv)
    rcv_thread.start()    
    send_thread=threading.Thread(target=msg_send)
    send_thread.start()
            

            