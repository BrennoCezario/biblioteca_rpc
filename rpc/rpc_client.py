import socket
import threading

SERVER_IP = '127.0.0.1'
SERVER_PORT = 5001

BINDER_IP = '127.0.0.1'
BINDER_PORT = 5000

class Client:
    def __init__(self):
        pass
    
    def start_service_search(self):
        search_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        search_socket.connect((BINDER_IP, BINDER_PORT))

        msg = "LOOKUP|math"

        search_socket.send(msg.encode())
        response = search_socket.recv(1024).decode()
        print(response)
    
    def start_client(self):
        self.start_service_search()
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((SERVER_IP, SERVER_PORT))

        msg = "Olá servidor"

        client_socket.send(msg.encode())

if __name__ == "__main__":
    client = Client()
    client.start_client()