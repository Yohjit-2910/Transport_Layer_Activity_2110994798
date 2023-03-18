from socket import *
serverPort = 11510

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print("The server is listening")

while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    ClientSendMessage1 = str.upper(message.decode("utf-8")) + " is received "
    serverSocket.sendto(ClientSendMessage1.encode(),clientAddress)

