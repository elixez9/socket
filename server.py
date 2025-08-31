import socket

server_ip = "127.0.0.1"
server_port = 8080


def run_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_ip, server_port))
    server_socket.listen(0)  #چک کن back log
    print(f"Server listening on {server_ip}:{server_port}")
    client_socket, client_address = server_socket.accept()
    print(f"Accepted connection from {client_address[0]} :{client_address[1]}")

    while True:
        request = client_socket.recv(1024)
        request = request.decode("utf-8")  #تبدیل کردن بایت
        if request == "close":  #اگر clientپیغام colse داد ببند
            client_socket.send(b"close".encode("utf-8"))
            break

        print(f"Received {request}")
    client_socket.close()
    server_socket.close()


run_server()
