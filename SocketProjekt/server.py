import socket
import threading
import json
# https://www.youtube.com/watch?v=3QiPPX-KeSc
# https://www.geeksforgeeks.org/socket-programming-multi-threading-python/


# 
HEADER = 64
FORMAT = 'utf-8'

SERVER, PORT = "127.0.0.1", 5050
#SERVER = socket.gethostbyname(socket.gethostname())
DISCONNECT_MESSAGE = "!Disconnect"


def handle_client(conn, addr):  
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
                
            print(f"[{addr}] {msg}")
            conn.send("Msg received".encode(FORMAT))


    conn.close()



def main():
    ADDR = (SERVER, PORT)

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)

    server.listen()
    print(f"[LISTENING] Server ist listening on {SERVER}:{PORT}")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


if __name__ == "__main__":
    print("[Starting] server is starting...")
    main()
