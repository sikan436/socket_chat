import socket,threading,sys
ip_addr='127.0.0.1'
port=12345
server=socket.socket()
alias=input("enter your alias")
server.connect((ip_addr,port))
if alias=='admin':
    password=input('enter admin password')
# if alias=='admin':
#     pwd=input('identify yourself if you are admin ,enter password')

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
                # nxt_msg=server.send(pwd.encode('ascii'))
                # if nxt_msg=='enter password?':
                #     server.send(pwd.encode("ascii"))
                #     if server.recv(1024).decode('ascii')=='Refuse':
                #         print("wrong password admin")
                #         sys.exit(0)
                        
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
            

            