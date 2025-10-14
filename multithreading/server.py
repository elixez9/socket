import socket
import threading

server_ip = "127.0.0.1"
server_port = 8080


def handle_client(client_socket, client_address):
    try:
        while True:
            request = client_socket.recv(1024).decode("utf-8")
            if request == "close":
                client_socket.send("close".encode("utf-8"))
                break
        print(f"Received {request}")
        client_socket.send("accepted".encode("utf-8"))
    except Exception as e:
        print(f"ERROR handling client: {e}")
    finally:
        client_socket.close()
        print(f"Connecting to client {client_address[0]} : {client_address[1]} closed")


def run_server():
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((server_ip, server_port))
        server_socket.listen(0)
        print(f"Server listening on {server_ip}:{server_port}")

        while True:
            client_socket, client_address = server_socket.accept()
            print(f"Accepted connection from {client_address[0]} : {client_address[1]}")
            ##Using the threading module and automatically creating it to connect multiple clients
            thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
            thread.start()

    except Exception as e:
        print(f"ERROR: {e}")
    finally:
        server_socket.close()

run_server()
