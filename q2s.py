# Import socket module
import socket

# Create a UDP socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = ('localhost', 12345)
s.bind(server_address)
print("Server is listening on port", server_address[1])

# Handle requests from clients
while True:
    # Receive a request from a client
    request, address = s.recvfrom(1024)
    print("Received request from", address)
    print("Request:", request.decode())

    # Parse the request and perform the operation
    tokens = request.decode().split()
    if tokens[0] == "append":
        # Append the two strings and send the result
        x = tokens[1]
        y = tokens[2]
        result = x + y
        s.sendto(result.encode(), address)
    else:
        # Send an error message if the request is invalid
        s.sendto("Invalid request".encode(), address)
