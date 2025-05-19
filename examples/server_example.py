import os
from rpc.rpc_server import Server

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== Servidor de Exemplo RPC ===")
    
    server_ip = '127.0.0.1' 
    service_name = "math"
    
    server = Server(server_ip)
    server.start_service_register(service_name)
    server.start_server()