#Sockets in Python

#import built-in python sockets lib
import socket

#create a connection to port 80(HTTP)
mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.connect(('data.pr4e.org', 80))

#An HTTP Request
cmd= 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysocket.send(cmd)

#while loop to check if document contains stuff and print it
while True:
    data = mysocket.recv(512)
    if (len(data)< 1):
        break
    print(data.decode())
mysocket.close()