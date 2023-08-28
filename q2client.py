import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((socket.gethostname(), 12345))
print("Connected to server")
while True:
    print("\nSelect an Operation:")
    print("0: Addition")
    print("1: Subtraction")
    print("2: Multiplication")
    print("3: Division")
    print("4: Logarithm base 10")
    print("5: Logarithm base 2")
    print("6: Modulo operation")
    op_index = int(input("Enter operation Index:"))
    if op_index < 0 or op_index > 6:
        print("Invalid operation index.")
        continue
    operands = input("Enter operands seperated by commas: ")
    operands = [float(operand.strip()) for operand in operands.split(',')]
    data = f"{op_index},{','.join(map(str, operands))}"
    client_socket.send(data.encode())
    result = client_socket.recv(1024).decode()
    print("Result:",result)
    again = input("another? (y/n): ")
    if again.lower() != "y":
        break
client_socket.close()
