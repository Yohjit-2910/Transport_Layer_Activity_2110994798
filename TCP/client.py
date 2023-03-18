import socket

# define the host and port
HOST = 'localhost'
PORT = 12345

# create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to the server
client_socket.connect((HOST, PORT))

# send a message to the server
message = "Hello SIT202, Message from Yohjit Chopra"
client_socket.send(message.encode())

# receive the response from the server
response = client_socket.recv(1024).decode()

# close the socket
client_socket.close()

# print the response from the server
print(response)
