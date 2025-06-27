import socket
import threading

# Function to handle client messages
def handle_client(client_socket):
    while True:
        try:
            # Receive the message from the client
            msg = client_socket.recv(1024).decode('utf-8')
            if msg:
                print(f"Message received: {msg}")
                broadcast(msg, client_socket)
            else:
                break
        except:
            break

# Function to broadcast messages to all connected clients
def broadcast(msg, current_client):
    for client in clients:
        if client != current_client:
            try:
                client.send(msg.encode('utf-8'))
            except:
                client.close()
                clients.remove(client)

# Set up the server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 12345))
server.listen(5)

clients = []

print("Server is running...")

# Accept connections and handle clients
while True:
    client_socket, client_address = server.accept()
    print(f"New connection: {client_address}")
    clients.append(client_socket)
    client_handler = threading.Thread(target=handle_client, args=(client_socket,))
    client_handler.start()
