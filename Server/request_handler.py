import socket, pickle
import threading
import game
from cards import Card

HOST = 'localhost'
PORT = 1234
BUFFER_SIZE = 1024

# create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the socket to a public host, and a port
server_socket.bind((HOST, PORT))

# become a server socket
server_socket.listen(5)
print(f"Server is listening on port {PORT}")

# create a list to store all connected clients
clients = []
lobbys = []

def handle_client(client_socket, client_address):
    print(f"Connection from {client_address} has been established!")
    clients.append(client_socket)
    

    while True:
        try:
            # receive data from client
            data = client_socket.recv(BUFFER_SIZE)
            if data:
                vecchia = pickle.loads(data)
                print(vecchia.get_priority())
                
                
                
                #print(f"Received data: {data.decode()}")
                # broadcast the received message to all clients
                #for c in clients:
                #if c != client_socket:
                #c.send(data)
            else:
                # if the client socket is closed, remove it from the list of clients
                clients.remove(client_socket)
                print(f"Connection from {client_address} has been closed!")
                break
        except:
            # if an exception is thrown, close the socket and remove it from the list of clients
            client_socket.close()
            clients.remove(client_socket)
            print(f"Connection from {client_address} has been closed!")
            break

while True:
    # wait for client connections
    client_socket, client_address = server_socket.accept()
    # create a new thread to handle the client connection
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_thread.start()
