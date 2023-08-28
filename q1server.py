import socket

# Create a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_address = ('localhost', 12345)
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(1)
print("Chatbot server is waiting for a connection...")

# Accept a connection
client_socket, client_address = server_socket.accept()
print("Connected to:", client_address)

# Chatbot responses
responses = {
    "hello": "Hello! Welcome to our book store. How can I assist you today?",
    "books": "We have a wide range of books available. What genre are you interested in?",
    "recommendation": "Sure, I can help with that. Based on your preferences, I recommend...",
    "thank you": "You're welcome! If you have any more questions, feel free to ask.",
    "bye": "Goodbye! Have a great day.",
}

try:
    while True:
        # Receive data from the client
        data = client_socket.recv(1024).decode()
        if not data:
            break
        
        # Process the received message and generate a response
        response = responses.get(data.lower(), "I'm sorry, I didn't understand that.")

        # Send the response back to the client
        client_socket.send(response.encode())
        print("Client:", data)
        print("Chatbot:", response)

finally:
    # Clean up the connection
    client_socket.close()
    server_socket.close()
