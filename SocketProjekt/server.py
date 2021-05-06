import socket
import threading
import json
# https://www.youtube.com/watch?v=3QiPPX-KeSc
# https://www.geeksforgeeks.org/socket-programming-multi-threading-python/


# 
HEADER = 64
FORMAT = 'utf-8'

SERVER, PORT = "127.0.0.1", 12345
#SERVER = socket.gethostbyname(socket.gethostname())
DISCONNECT_MESSAGE = "!Disconnect"

list_of_clients = []
list_of_nicknames = []
groups = []


def broadcastToGroup():
    return 0

def broadcast(msg):
    for client in list_of_clients:
        client.send(msg)

def handle_client(client, addr):  
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_length = client.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = client.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
                
            print(f"[{addr}] {msg}")
            client.send("Msg received".encode(FORMAT))


    index = list_of_clients.index(client)
    list_of_clients.remove(client)
    print("asdasd", list_of_clients)
    client.close()



def main():
    ADDR = (SERVER, PORT)

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)

    server.listen()
    print(f"[LISTENING] Server ist listening on {SERVER}:{PORT}")

    while True:
        client, addr = server.accept()


        # Request And Store Nickname
        client.send('setNickname'.encode(FORMAT))
        nickname = client.recv(1024).decode(FORMAT)

        list_of_clients.append(client)
        thread = threading.Thread(target=handle_client, args=(client, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


if __name__ == "__main__":
    print("[Starting] server is starting...")
    main()
