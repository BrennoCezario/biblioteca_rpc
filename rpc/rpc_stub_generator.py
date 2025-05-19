import socket
import serializer

class MathStub:
    def __init__(self, server_ip, server_port):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((server_ip, server_port))
        
        self.codec = serializer.Serializer()
        
    def add(self, x, y):
        return self.process_function("add", x, y)
    
    def sub(self, x, y):
        return self.process_function("sub", x, y)
    
    def multiply(self, x, y):
        return self.process_function("multiply", x, y)
    
    def divide(self, x, y):
        return self.process_function("divide", x, y)
        
    def process_function(self, function, x, y):
        serialized_message = self.codec.serialize_function(function, x, y)
        self.client_socket.send(serialized_message)
        
        response = self.client_socket.recv(1024)
        msg_type, operation_result = self.codec.desserialize_result(response)
    
        if msg_type == "RESULT":
            return operation_result
        else:
            return "Erro na troca de informações com o servidor"
    