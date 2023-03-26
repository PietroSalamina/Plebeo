import socket, pickle
import threading
import player
import cards


HOST = 'localhost'
PORT = 1234
BUFFER_SIZE = 1024

# create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client socket to the server
client_socket.connect((HOST, PORT))

#Send startin information from client
vecchia = cards.Card(8, "Swords")
message = pickle.dumps(vecchia)
client_socket.send(message)

# define a function to handle receiving data from the server
def receive_data():
    while True:
        try:
            # receive data from server
            data = client_socket.recv(BUFFER_SIZE)
            if data:
                print(f"Received data: {data.decode()}")
            else:
                # if the server socket is closed, exit the loop
                break
        except:
            # if an exception is thrown, exit the loop
            break

# create a new thread to handle receiving data from the server
receive_thread = threading.Thread(target=receive_data)
receive_thread.start()

# loop to send data to the server
while True:
    
    # send data to the server
    #client_socket.send(message.encode())
    if message == "exit":
        # if the user types "exit", close the client socket and exit the loop
        client_socket.close()
        break
