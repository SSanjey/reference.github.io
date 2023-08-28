import socket
import math
def perform_operation(op_index, operands):
    if op_index == 0:
        return operands[0]+ operands[1]
    elif op_index == 1:
        return operands[0]- operands[1]
    elif op_index == 2:
        return operands[0]* operands[1]
    elif op_index == 3:
        return operands[0] / operands[1]
    elif op_index == 4:
        return math.log10(operands[0])
    elif op_index == 5:
        return math.log2(operands[0])
    elif op_index == 6:
        return operands[0] % operands[1]
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((socket.gethostname(), 12345))
server_socket.listen(1)
client_socket, client_address = server_socket.accept()
print("Connection from:", client_address)
while True:
    data = client_socket.recv(1024).decode()
    if not data:
        break
    try:
        data_list = data.split(",")
        op_index = int(data_list[0])
        operands = [float(operand) for operand in data_list[1:]]
        result = perform_operation(op_index, operands)
        client_socket.send(str(result).encode())
    except Exception as e:
        client_socket.send("Error: Invalid input or operation.".encode())
client_socket.close()
