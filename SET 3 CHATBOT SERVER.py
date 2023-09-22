import socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('localhost', 12345))
client_data, client_address = server_socket.recvfrom(1024)
client_data = client_data.decode()
print('Client:', client_data)
server_data = 'Welcome to the school admission chatbot. I can help you with the admission process for your child for standard 5.'
server_socket.sendto(server_data.encode(), client_address)

while True:
    client_data, client_address = server_socket.recvfrom(1024)
    client_data = client_data.decode()
    print('Client:', client_data)
    if client_data == 'quit':
        break
    server_data = 'Please ask me a question about the admission process for standard 5.'
    server_socket.sendto(server_data.encode(), client_address)
server_socket.close()
