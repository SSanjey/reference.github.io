import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 12345)
client_data = 'Hello school administration. I would like to enquire about the admission process for my child for standard 5.'
client_socket.sendto(client_data.encode(), server_address)
server_data, server_address = client_socket.recvfrom(1024)
server_data = server_data.decode()
print('Server:', server_data)
while True:
    client_data = input('Client: ')
    client_socket.sendto(client_data.encode(), server_address)
    server_data, server_address = client_socket.recvfrom(1024)
    server_data = server_data.decode()
    print('Server:', server_data)
    if client_data == 'quit':
        break
client_socket.close()
