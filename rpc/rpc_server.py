import socket
import threading
import os
from rpc import serializer
from interface import math_service

HOST = '127.0.0.1'
PORT = 5001

BINDER_IP = '127.0.0.1'
BINDER_PORT = 5000

class Server:
    def __init__(self):
        pass
    
    def handle_client(self, conn, addr):
        while True:
            try:
                message = conn.recv(1024)
                
                if not message:
                    continue
                
                print(f"Mensagem recebida do endereço {addr}: {message}")
                
                codec = serializer.Serializer()
                function_name, args = codec.desserialize_function(message)
                print(f"Mensagem Desserializada: {function_name, args}")
                
                math = math_service.DistributedCalculator()
                result = None
                
                match function_name:
                    case "add":
                        result = math.add(*args)
                    case "sub":
                        result = math.sub(*args)
                    case "multiply":
                        result = math.multiply(*args)
                    case "divide":
                        result = math.divide(*args)
                
                
                print(f"Resultado da Operação: {result}\n")
                serialized_message = codec.serialize_result(result)
                conn.send(serialized_message)
            except Exception:
                conn.send(codec.serialize_result(f"ERROR:{str(Exception)}"))
                
    def start_service_register(self):
        register_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        register_socket.connect((BINDER_IP, BINDER_PORT))

        register_message = f"REGISTER|math|{HOST}|{PORT}"
        print(f"\nIniciando registro de serviço com {register_message}\n")

        register_socket.send(register_message.encode())
        register_response = register_socket.recv(1024).decode()
        print("Um serviço com esse nome já está registrado\n" if register_response == "ERRO" else "Serviço Registrado com sucesso\n")
        
    def start_server(self):
        self.start_service_register()
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((HOST, PORT))
        server_socket.listen()

        print("Servidor iniciado, aguardando conexões...\n")

        while True:
            conn, addr = server_socket.accept()
            print(f"Conexão estabelecida com {addr}")
            threading.Thread(target=self.handle_client, args=(conn, addr), daemon=True).start()

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    server = Server()
    server.start_server()