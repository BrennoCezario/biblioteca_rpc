import socket
import threading
import importlib
import random
from . import rpc_stub_generator as stub

BINDER_IP = '127.0.0.1'
BINDER_PORT = 5000

services = [
    'math'
]

class Server:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.service_stub = any
       
    def handle_client(self, conn, addr):
        while True:
                message = conn.recv(1024)
                
                if not message:
                    continue
                
                print(f"Mensagem recebida do endereço {addr}: {message}")
                
                response = self.service_stub.process_message(message)

                conn.send(response)
                
    def generate_stub(self, service_name):
        stub_generator = stub.StubGenerator()
        stub_generator.generate_stub(service_name, "server")
        
        stub_module_name = f"rpc.server_{service_name}_stub"
        module = importlib.import_module(stub_module_name)
        self.service_stub = getattr(module, f"{service_name.capitalize()}ServerStub")()
                
    def start_service_register(self, service_name):
        self.service_name = service_name
        self.generate_stub(service_name)
        
        register_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        register_socket.connect((BINDER_IP, BINDER_PORT))

        if service_name in services:
            print("Vamos iniciar o registro de um serviço!")
            register_message = f"REGISTER|{self.service_name}|{self.ip}|{self.port}"
        else:
            print("Serviço indisponível para o registro")
            return
        
        print(f"\nIniciando registro de serviço com {register_message}\n")

        register_socket.send(register_message.encode())
        register_response = register_socket.recv(1024).decode()
        if register_response == "ERRO":
            print("Um serviço com esse nome já está registrado\n")
        else:
            print("Serviço Registrado com sucesso\n")
        
        self.start_server()
        
    def start_server(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((self.ip, self.port))
        server_socket.listen()

        print("Servidor iniciado, aguardando conexões...\n")

        while True:
            conn, addr = server_socket.accept()
            print(f"Conexão estabelecida com {addr}")
            threading.Thread(target=self.handle_client, args=(conn, addr), daemon=True).start()