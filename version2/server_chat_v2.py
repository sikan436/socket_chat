import socket 
import sys

s=socket.socket()
print ("socket connected succesfully")

port = 12345  
s.bind(('',port))
print (f"socket binded to {port} successfully")
while True:
    s.listen(5)

    print ("socket listening")


    c,addr=s.accept()
    name=input("type your message here")
    print (f"got connection from {addr}")
    c.send(f'Thank you for connecting {name}'.encode()) 
    c.close()
    break

 