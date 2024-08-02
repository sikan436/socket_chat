import socket 
import sys

s=socket.socket()
print ("socket connected succesfully")

port = 12345  
s.bind(('',port))
print (f"socket binded to {port} successfully")

s.listen(5)

print ("socket listening")

while True:
    c,addr=s.accept()
    print (f"got connection from {addr}")
    c.send('Thank you for connecting'.encode()) 
    c.close()
    break

 