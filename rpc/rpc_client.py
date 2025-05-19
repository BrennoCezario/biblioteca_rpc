import socket
import threading
import os
import rpc_stub_generator as stub

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
        search_response = search_socket.recv(1024).decode()
        
        if search_response == "ERRO":
            print("\nServiço não encontrado!")
        else:
            print(f"\nServiço Encontrado e localizado em {search_response}")
            message_parts = search_response.split("|")
            server_ip, server_port = message_parts[0], int(message_parts[1])
            math = stub.MathStub(server_ip,server_port)
            print(f"Resultado de 4 + 2: {math.add(4,2)}")
            print(f"Resultado de 4 - 2: {math.sub(4,2)}")
            print(f"Resultado de 4 * 2: {math.multiply(4,2)}")
            print(f"Resultado de 4 / 0: {math.divide(4,0)}")
            
            
    
    def start_client(self, server_ip, server_port):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((server_ip, server_port))

        msg = "Olá servidor"

        client_socket.send(msg.encode())

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    client = Client()
    client.start_service_search()