import socket
from threading import Thread

server = None
port = None
ip = None

clients = {}

def acceptConnections():
    global clients
    global server

    while True:
        playerSocket, addr = server.accept()
        playerName = playerSocket.recv(1024).decode().strip()

        print(playerName)

        if(len(clients.key()) == 0):
            clients[playerName] = {'playerType: player1'}
        else:
            clients[playerName] = {'playerType: player2'}

        clients[playerName]["playerSocket"] = playerSocket
        clients[playerName]["address"] = addr
        clients[playerName]["playerName"] = playerName
        clients[playerName]["turn"] = False

        print(f"Connection made with {playerName}:{addr}")

def setup():
    print('\n\t\t\t\t\t\****Welcome to Tambola Game****\n"')

    global server
    global port
    global ip

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip, port))
    server.listen(10)

    print("\nserver waiting for connections")

