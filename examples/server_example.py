import os
from rpc.rpc_server import Server
from interface import math_service

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== Servidor de Exemplo RPC ===")
    
    service_name = "math"
    
    server_ip = '127.0.0.1' 
    
    server = Server(service_name, server_ip)
    server.start_server()