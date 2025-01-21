import socket
import threading

def receive_messages(client):
    """Nepřetržitě přijímá zprávy od serveru a vypisuje je."""
    while True:
        try:
            message = client.recv(1024).decode()
            if not message:
                break
            print(message)
        except:
            print("Disconnected from server.")
            client.close()
            break

def start_client():
    """Spustí klienta a připojí se k serveru."""
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("127.0.0.1", 12345))  # Připojení k serveru

    # Čekáme na výzvu k zadání uživatelského jména
    username_prompt = client.recv(1024).decode()
    print(username_prompt, end="")  # Zobrazíme výzvu od serveru
    username = input()
    client.send(username.encode())

    # Čekáme na výzvu k zadání hesla
    password_prompt = client.recv(1024).decode()
    print(password_prompt, end="")  # Zobrazíme výzvu od serveru
    password = input()
    client.send(password.encode())

    # Odpověď serveru (úspěšné/neúspěšné přihlášení)
    response = client.recv(1024).decode()
    print(response)

    if "Login successful" not in response:
        client.close()
        return

    threading.Thread(target=receive_messages, args=(client,), daemon=True).start()

    while True:
        message = input()
        if message.lower() == "exit":
            client.close()
            break
        client.send(message.encode())

if __name__ == "__main__":
    start_client()