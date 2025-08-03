import socket
import re


def calculate(operation, a, b):
    if operation == "SOMMA":
        return a + b
    elif operation == "DIFFERENZA":
        return a - b
    elif operation == "POTENZA":
        return a**b
    elif operation == "PRODOTTO":
        return a * b
    elif operation == "DIVISIONE_INTERA":
        return a // b
    else:
        return None


def main():
    host = "2048.challs.olicyber.it"
    port = 10007

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        data = s.recv(1024).decode()
        print(data)

        while True:
            match = re.search(r"(\w+) (\d+) (\d+)", data)
            if not match:
                break

            operation, a, b = match.groups()
            a, b = int(a), int(b)
            result = calculate(operation, a, b)

            if result is not None:
                s.sendall(f"{result}\n".encode())
                data = s.recv(1024).decode()
                print(data)
            else:
                print("Operazione non riconosciuta")
                break


if __name__ == "__main__":
    main()