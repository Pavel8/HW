import socket
import threading

# Simulovaná databáze uživatelů (username: password)
USERS = {
    "user1": "password1",
    "user2": "password2",
    "user3": "password3"
}

clients = {}  # Mapuje sockety klientů na jejich uživatelská jména

def broadcast(message, sender=None):
    """Pošle zprávu všem připojeným klientům kromě odesílatele."""
    for client in list(clients.keys()):
        if client != sender:
            try:
                client.send(message.encode())
            except:
                client.close()
                del clients[client]

def handle_client(client):
    """Obsluhuje jednoho klienta."""
    try:
        # Odeslání výzvy pro username a jeho příjem
        client.send("Enter username: ".encode())
        username = client.recv(1024).decode().strip()

        # Odeslání výzvy pro password a jeho příjem
        client.send("Enter password: ".encode())
        password = client.recv(1024).decode().strip()

        if USERS.get(username) == password:
            client.send("Login successful! Welcome to the chat.\n".encode())
            clients[client] = username
            broadcast(f"{username} has joined the chat!", client)
        else:
            client.send("Invalid credentials. Disconnecting...\n".encode())
            client.close()
            return

        while True:
            message = client.recv(1024).decode()
            if not message:
                break
            broadcast(f"{username}: {message}", client)

    except ConnectionResetError:
        pass
    finally:
        print(f"{clients.get(client, 'Unknown user')} disconnected.")
        broadcast(f"{clients.get(client, 'Unknown user')} has left the chat.", client)
        if client in clients:
            del clients[client]
        client.close()

def start_server():
    """Spustí server a čeká na připojení klientů."""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 12345))
    server.listen(5)
    print("Server is running on port 12345...")

    while True:
        client, addr = server.accept()
        print(f"New connection from {addr}")
        threading.Thread(target=handle_client, args=(client,)).start()

if __name__ == "__main__":
    start_server()
