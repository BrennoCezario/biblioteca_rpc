import socket
import threading
import os

HOST = '127.0.0.1'
PORT = 5000

services = []

class Binder:
    def __init__(self):
        pass
    
    def search_service(self, service_name, addr):
        print(f"Client ({addr})| Procurando Serviço '{service_name}'")
        for service in services:
            if service["service_name"] == service_name:
                print(f"Client ({addr})| Serviço '{service_name}' encontrado")
                return service["ip"] + "|" + service["port"]
        print(f"Client ({addr})| Erro: Serviço não encontrado!")
        return "ERRO"
    
    def register_service(self, service_name, ip, port, addr):
        print(f"Server ({addr})| Registrando Serviço '{service_name}'")
        if any(service["service_name"] == service_name for service in services):
            print(f"Server ({addr})| Erro: Serviço '{service_name}' já está registrado.")
            return "ERRO"
        else:
            service = {
                "service_name": service_name,
                "ip": ip,
                "port": port
            }
            services.append(service)
            print(f"Server ({addr})| Serviço '{service_name}' registrado com sucesso no binder.")
            return "REGISTERED"
        
    
    def handle_connections(self, conn, addr):
        while True:
            message = conn.recv(1024).decode()
            
            if not message:
                continue
            
            print(f"Mensagem recebida do endereço {addr}: {message}")
            
            message_fields = message.split("|")
            
            if "REGISTER" in message_fields:
                register_response = self.register_service(message_fields[1], message_fields[2], message_fields[3], addr)
                print("\n")
                conn.send(register_response.encode())
            
            elif "LOOKUP" in message_fields:
                search_response = self.search_service(message_fields[1], addr)
                conn.send(search_response.encode())
                print("\n")
            
            else:
                print(f"Client/Server(addr)| A mensagem '{message}'  é inválida\n")

    def start_binder(self):
        binder_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        binder_socket.bind((HOST, PORT))
        binder_socket.listen()

        print("\nBinder iniciado, aguardando conexões...\n")

        while True:
            conn, addr = binder_socket.accept()
            print(f"Conexão estabelecida com {addr}")
            threading.Thread(target=self.handle_connections, args=(conn, addr), daemon=True).start()

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    binder = Binder()
    binder.start_binder()
