import socket
import threading

def handle_client(conn , addr):
    print(f"Client connected: {addr}")
    while True:
        try:
            message = conn.recv(1024).decode('utf-8')
            if not message:
                print(f"Client disconnected: {addr}")
                break
            print(f"{message.strip()}")
        except Exception as e:
            print(f"Error with client {addr}: {e}")
            break
    conn.close()

def start_server(host, port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    print(f"Server started on {host}:{port}")
    server.listen()

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

if __name__ == "__main__":
    start_server('localhost', 8080)