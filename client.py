import socket

handlerSocket = socket.socket()
serverIP = "127.0.0.1"
serverPort = 2222

handlerSocket.connect((serverIP,serverPort))
print('Connected to Server')

while True:
    message = handlerSocket.recv(1024)
    print('Message from Server : ', message.decode())
    message = input("Type message : ")
    handlerSocket.send(message.encode('utf-8'))
    pass