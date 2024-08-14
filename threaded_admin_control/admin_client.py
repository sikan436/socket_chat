import socket,threading
ip_addr='127.0.0.1'
port=12345
server=socket.socket()
aliases=[]
clients=[]
alias=input("enter your alias")
server.connect((ip_addr,port))


def msg_rcv():
    while True:
        try:
            msg=server.recv(1024)
            msg=msg.decode('utf-8')
            if msg=='your nickname?':
                server.send(alias.encode("utf-8"))
            elif msg=='enter password?':
                pwd=input('enter password')
                server.send(pwd.encode('utf-8'))
            else:   
                print(msg)
            
        except:
            print("error")
            server.close()
            break

def msg_send():
    while True:
        try:
            msg=f'{alias}:{input("")}'
            server.send(msg.encode('utf-8'))
        except:
            print ("connection lost")
            server.close()
            break

if __name__=='__main__':
    rcv_thread=threading.Thread(target=msg_rcv)
    rcv_thread.start()    
    send_thread=threading.Thread(target=msg_send)
    send_thread.start()
            

            

