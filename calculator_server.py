import socket

operators = ["+", "-", "*", "/"]

def calculate(expression):
    try:
        op1, operator, op2 = expression.split()
        op1 = float(op1)
        op2 = float(op2)

        if operator == "+":
            return op1 + op2
        elif operator == "-":
            return op1 - op2
        elif operator == "*":
            return op1 * op2
        elif operator == "/":
            if op2 == 0:
                return "Error: Division by zero"
            return op1 / op2
        else:
            return "Error: Invalid operator"

    except Exception as e:
        return f"Error: {str(e)}"

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_socket.bind((socket.gethostname(), 12345))
print("Server listening")

while True:
    msg, client_address = server_socket.recvfrom(1024)
    msg = msg.decode()
    print(f"Client ({client_address}): {msg}")

    if msg.lower() == "bye":
        server_socket.sendto("Bye".encode(), client_address)
        break

    result = str(calculate(msg))
    server_socket.sendto(result.encode(), client_address)

server_socket.close()
