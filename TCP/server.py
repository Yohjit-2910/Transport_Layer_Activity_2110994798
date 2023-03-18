import socket
# define the host and port
HOST = 'localhost'
PORT = 12345

# create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the socket to a public host and port
server_socket.bind((HOST, PORT))

# listen for incoming connections
server_socket.listen(1)

# wait for a connection
print('Server is listening for connections...')
connection_socket, address = server_socket.accept()
print('Connected by', address)
# receive the message from the client
message = connection_socket.recv(1024).decode()
# count the characters in the message
num_chars = len(message)

# send the response to the client
response = f"{num_chars}, {message.upper()}"
connection_socket.send(response.encode())

# close the connection and the socket
connection_socket.close()
server_socket.close()
