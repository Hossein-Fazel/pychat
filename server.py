import socket
import threading

def handle_client(conn , addr):
    while True:
        try:
            message = conn.recv(1024).decode('utf-8')
            if not message:
                break

            elif message.startswith("<RECEIVE:"):
                splited = message.split(":")
                file_name, file_size = splited[1], int(splited[2])
                print(f"Receiving file '{file_name}' ({file_size} bytes)")

                with open(file_name, 'wb') as file:
                    remaining_bytes = file_size
                    while remaining_bytes > 0:
                        data = conn.recv(min(4096, remaining_bytes))
                        if not data:
                            break
                        file.write(data)
                        remaining_bytes -= len(data)
                print(f"File '{file_name}' received successfully.")

            else:
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