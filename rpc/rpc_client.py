import socket
import importlib
from . import rpc_stub_generator as stub

BINDER_IP = '127.0.0.1'
BINDER_PORT = 5000

class Client:
    def __init__(self):
        self.service_stub = any
        
    def generate_stub(self, service_name, server_ip, server_port):
        stub_generator = stub.StubGenerator()
        stub_generator.generate_stub(service_name,"client")
        
        stub_module_name = f"rpc.client_{service_name}_stub"
        module = importlib.import_module(stub_module_name)
        self.service_stub = getattr(module, f"{service_name.capitalize()}ClientStub")(server_ip, server_port)
    
    def start_service_search(self, service_name):
        search_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        search_socket.connect((BINDER_IP, BINDER_PORT))

        print("Vamos iniciar a busca por um serviço!")
        search_msg = f"LOOKUP|{service_name}"

        search_socket.send(search_msg.encode())
        search_response = search_socket.recv(1024).decode()
        
        if search_response == "ERRO":
            print("\nServiço não encontrado!")
        else:
            print(f"\nServiço Encontrado e localizado em {search_response}")

            message_parts = search_response.split("|")
            server_ip, server_port = message_parts[0], int(message_parts[1])
            self.generate_stub(service_name, server_ip, server_port)