import socket
import threading

HOST = '127.0.0.1'
PORT = 5001

BINDER_IP = '127.0.0.1'
BINDER_PORT = 5000

class Server:
    def __init__(self):
        pass
    
    def handle_client(self, conn, addr):
        message = conn.recv(1024).decode()
        print(f"Mensagem recebida do endereço {addr}: {message}")
    
    def start_service_register(self):
        register_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        register_socket.connect((BINDER_IP, BINDER_PORT))

        register_message = f"REGISTER|math|{HOST}|{PORT}"

        register_socket.send(register_message.encode())
        response = register_socket.recv(1024).decode()
        print(response)
        
    def start_server(self):
        self.start_service_register()
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((HOST, PORT))
        server_socket.listen()

        print("Servidor iniciado, aguardando conexões...")

        while True:
            conn, addr = server_socket.accept()
            print(f"Conexão estabelecida com {addr}")
            threading.Thread(target=self.handle_client, args=(conn, addr), daemon=True).start()

if __name__ == "__main__":
    server = Server()
    server.start_server()