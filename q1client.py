import socket

# Create a socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the client socket to the server
server_address = ('localhost', 12345)
client_socket.connect(server_address)

try:
    while True:
        # Send a message to the server (chatbot)
        message = input("You: ")
        client_socket.send(message.encode())
        
        # Receive and display the response from the server (chatbot)
        response = client_socket.recv(1024).decode()
        print("Chatbot:", response)
        
        # Exit the loop if the user says 'bye'
        if message.lower() == "bye":
            break

finally:
    # Clean up the connection
    client_socket.close()
