import socket
from time import sleep
import os
from PyBar.progressbar import progressbar

def send_file(ssocket, file):
    try:
        fname = os.path.basename(file)
        fsize = os.path.getsize(file)

        header = f"<RECEIVE:{fname}:{fsize}"
        ssocket.send(header.encode('utf-8'))
        pbar = progressbar("-", total= fsize,)
        with open(file, 'rb') as file:
            while True:
                data = file.read(4096)
                if not data:
                    break
                ssocket.send(data)
                
                pbar.update(len(data))
                pbar.show()
            pbar.stop()

        print(f"File '{fname}' sent successfully.")
    except Exception as e:
        print(f"Error sending file: {e}")

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

        elif message.startswith("<SEND "):
            file_path = message[6:len(message)-1]
            if os.path.exists(file_path):
                send_file(client_socket, file_path)
            else:
                print("File does not exist")

        else:
            message = f"{name} : " + message
            client_socket.send(message.encode('utf-8'))

    client_socket.close()

if __name__ == "__main__":
    start_client("localhost", 8080, "test_name")