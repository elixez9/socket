import socket

server_ip = "127.0.0.1"
server_port = 8080


def run_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))

    while True:
        msg = input("enter a message :")
        client_socket.send(msg.encode("utf-8")[:1024])

        response = client_socket.recv(1024)
        response = response.decode("utf-8")

        if response.lower() == "closed":
            break

        print(f" Received: {response}")

    client_socket.close()


run_client()
