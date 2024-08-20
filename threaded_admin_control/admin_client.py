import socket,threading,sys
ip_addr='127.0.0.1'
port=12345
server=socket.socket()
aliases=[]
clients=[]
alias=input("enter your alias")
server.connect((ip_addr,port))
if alias=='admin':
    pwd=input('identify yourself if you are admin ,enter password')


def msg_rcv():
    while True:
        try:
            msg=server.recv(1024)  #alias

            msg=msg
            if msg=='your nickname?':
                server.send(alias.encode('ascii'))
                nxt_msg=server.send(pwd.encode('ascii'))
                if nxt_msg=='enter password?':
                    server.send(pwd.encode("ascii"))
                    if server.recv(1024).decode('ascii')=='Refuse':
                        print("wrong password admin")
                        sys.exit(0)
                        
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
            

            