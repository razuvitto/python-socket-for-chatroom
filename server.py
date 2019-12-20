import socket

listenerSocket = socket.socket()
serverIP = "0.0.0.0"
serverPort = 2222
listenerSocket.bind((serverIP,serverPort))
listenerSocket.listen(0)
print('Server Ready')
while True:
    handlerSocket, addr = listenerSocket.accept()
    print('New client succesfully connected to server with address : ', addr)
    while True:
        message = input("Type message : ")
        handlerSocket.send(message.encode('utf-8'))
        message = handlerSocket.recv(1024)
        print('Message from client : ', message.decode())
        pass
    pass