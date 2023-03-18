import codecs
from socket import *
serverName = "127.0.0.1"
serverPort = 11510
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = "Hello SIT202_Yohjit_Chopra (2110994798)"
clientSocket.sendto(message.encode(),(serverName, serverPort))
ServerReply, serverAddress = clientSocket.recvfrom(2048)
print(ServerReply.decode())
clientSocket.close()

