# Import socket module
import socket

# Create a UDP socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Define the server address and port
server_address = ('localhost', 12345)

# Send the request to the server
request = input("Enter your request: ") # e.g. append hello world or append foo bar
s.sendto(request.encode(), server_address)

# Receive the response from the server
response, address = s.recvfrom(1024)
print("The server replied: ", response.decode())

# Close the socket
s.close()
