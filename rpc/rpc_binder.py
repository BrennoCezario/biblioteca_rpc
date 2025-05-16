import socket
import threading
import json

HOST = '127.0.0.1'
PORT = 5000

services = []

class Binder:
    def __init__(self):
        pass
    
    def search_service(self, service_name):
        print(f"Procurando Serviço '{service_name}'")
        for service in services:
            if service["service_name"] == service_name:
                print(f"Serviço '{service_name}' encontrado")
                return service
        return "Servico não encontrado"
    
    def register_service(self, service_name, ip, port):
        if any(service["service_name"] == service_name for service in services):
            print(f"Erro: Serviço '{service_name}' já está registrado.")
            return
        else:
            service = {
                "service_name": service_name,
                "ip": ip,
                "port": port
            }
            services.append(service)
            print(f"Serviço '{service_name}' registrado com sucesso no binder.")
        
    
    def handle_connections(self, conn, addr):
        while True:
            message = conn.recv(1024).decode()
            if message != "":
                print(f"Mensagem recebida do endereço {addr}: {message}")
                
                message_fields = message.split("|")
                print(message_fields)
                
                if "REGISTER" in message_fields:
                    self.register_service(message_fields[1], message_fields[2], message_fields[3])
                    conn.send(json.dumps(services).encode())
                
                elif "LOOKUP" in message_fields:
                    response = self.search_service(message_fields[1])
                    print(response)
                    conn.send(json.dumps(response).encode())
                
                else:
                    print(f" A mensagem '{message}'  é inválida")

    def start_binder(self):
        binder_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        binder_socket.bind((HOST, PORT))
        binder_socket.listen()

        print("Binder iniciado, aguardando conexões...")

        while True:
            conn, addr = binder_socket.accept()
            print(f"Conexão estabelecida com {addr}")
            threading.Thread(target=self.handle_connections, args=(conn, addr), daemon=True).start()

if __name__ == "__main__":
    binder = Binder()
    binder.start_binder()
