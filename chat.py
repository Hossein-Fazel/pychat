import threading
from server import start_server
from client import start_client
from json import load
from json_checker import Checker

config_schema = {
    "server" : str,
    "your_port" : int,
    "friend_port" : int
}

def main():
    print("\t\t*** Welcome to simple chat ***\n")
    try:
        with open("config.json", 'r') as jfile:
            config = load(jfile)
        Checker(config_schema).validate(config)
        print("Config load successfully")
    except FileNotFoundError:
        print("The config file is missing")
        exit()
    except:
        print("The config file is corrupt")
        exit()
    name = input("Please enter your name : ")


    
    lthread = threading.Thread(target=start_server, args=(config["server"], config["your_port"]))
    tthread = threading.Thread(target=start_client, args=(config["server"], config["friend_port"], name))
    lthread.start()
    tthread.start()


if __name__ == "__main__":
    main()