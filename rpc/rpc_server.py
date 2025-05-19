import socket
import threading
import os
from . import serializer
from interface import math_service

BINDER_IP = '127.0.0.1'
BINDER_PORT = 5000

class Server:
    def __init__(self, service_name, ip):
        self.ip = ip
        self.service_name = service_name
        self.port = 5001
    
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

        print("Vamos iniciar o registro de um serviço!")
        register_message = f"REGISTER|{self.service_name}|{self.ip}|{self.port}"
        
        print(f"\nIniciando registro de serviço com {register_message}\n")

        register_socket.send(register_message.encode())
        register_response = register_socket.recv(1024).decode()
        if register_response == "ERRO":
            print("Um serviço com esse nome já está registrado\n")
        else:
            print("Serviço Registrado com sucesso\n")
        
    def start_server(self):
        self.start_service_register()
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((self.ip, self.port))
        server_socket.listen()

        print("Servidor iniciado, aguardando conexões...\n")

        while True:
            conn, addr = server_socket.accept()
            print(f"Conexão estabelecida com {addr}")
            threading.Thread(target=self.handle_client, args=(conn, addr), daemon=True).start()