import socket
from time import sleep

def start_client(server, port, name):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    while True:
        try:
            client_socket.connect((server, port))
            print("Your friend is online")
            break
        except:
            print("Your friend is offline")
            sleep(2)

    while True:
        message = input()
        if message.lower() == 'exit':
            break
        message = f"{name} : " + message
        client_socket.send(message.encode('utf-8'))

    client_socket.close()

if __name__ == "__main__":
    start_client("localhost", 8080, "test_name")