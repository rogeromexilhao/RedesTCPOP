import socket
import threading

choice = input("Host = (1) ou Client = (2)")

if choice == '1':
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('192.168.15.32', 5000))
    server.listen()

    client, _ = server.accept()
elif choice == '2':
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('192.168.15.32', 5000))
else:
    exit()

def sending_mensages(c):
    while True:
            message = input("")
            c.send(message.encode())
            print("You: " + message)

def receiving_mensages(c):
     while True:
            print("Partner: " + c.recv(1024).decode())

threading.Thread(target=sending_mensages, args=(client,)).start()
threading.Thread(target=receiving_mensages, args=(client,)).start()