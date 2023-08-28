import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

serverAddressPort = (socket.gethostname(), 12345)

print("Select an operator: +, -, *, /")
operator = input("Client: ")

while operator not in ['+', '-', '*', '/']:
    print("Invalid operator. Select an operator: +, -, *, /")
    operator = input("Client: ")

while True:
    operand1 = input("Enter the first operand: ")
    operand2 = input("Enter the second operand: ")

    if not operand1.isdigit() or not operand2.isdigit():
        print("Invalid operands. Please enter valid numeric operands.")
        continue

    message = f"{operand1} {operator} {operand2}"

    client_socket.sendto(message.encode(), serverAddressPort)

    if operator == "Bye":
        break

    result, addr = client_socket.recvfrom(1024)
    print(f"Server {addr}: Result = {result.decode()}")

client_socket.close()
