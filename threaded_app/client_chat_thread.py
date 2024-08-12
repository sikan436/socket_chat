import socket,threading
ip_addr='127.0.0.1'
port=12345
server=socket.socket()
aliases=[]
clients=[]
alias=input("enter your alias")
server.connect((ip_addr,port))


def run_client():
    while True:
        message=input("type message")
        server.send(f"{alias}:message".encode("utf-8"))
        
if __name__=="__main__":
    run_client()
