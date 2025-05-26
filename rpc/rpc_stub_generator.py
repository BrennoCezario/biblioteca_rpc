import socket
import os
import re
from . import serializer

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INTERFACE_DIR = os.path.join(BASE_DIR, "..", "interface")

class StubGenerator:
    def __init__(self):
        pass

    def read_service(self, service_name):
        file_name = service_name +"_service.py" 
        datapath = os.path.abspath(os.path.join(INTERFACE_DIR, file_name))
        
        with open(datapath, "r") as file:
            content = file.read()
        return content

    def select_functions(self, content):
        functions = []
        function_matches = re.findall(r'def (\w+)\(', content)
        class_match = re.findall(r'class (\w+)\:', content)
        service_class = class_match[0] if class_match else None
        
        functions.extend(function_matches)
        
        return functions, service_class
    
    def write_stub(self, functions, service_class, stub_type, service_name):
        datapath = os.path.abspath(os.path.join(BASE_DIR, f"{stub_type}_{service_name}_stub.py"))
        
        with open(datapath, "w") as file:
            file.write(f"import socket\n" if stub_type == "client" else f"from interface import {service_name}_service\n")
            file.write(f"from . import serializer\n\n")
            file.write(f"class {service_name.capitalize()}{stub_type.capitalize()}Stub:\n")
            
            for function in functions:
                if function == "__init__":
                    file.write(f"\tdef {function}(self, server_ip, server_port):\n" if stub_type == "client" else f"\tdef {function}(self):\n")
                    file.write(f"\t\tself.{stub_type}_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)\n" if stub_type == "client" else "\t\tself.codec = serializer.Serializer()\n") 
                    file.write(f"\t\tself.{stub_type}_socket.connect((server_ip, server_port))\n" if stub_type == "client" else f"\t\tself.service = {service_name}_service.{service_class}()\n")
                    file.write(f"\t\tself.codec = serializer.Serializer()\n\n" if stub_type == "client" else "\t\tpass\n")
                    continue
                
                file.write(f"\tdef {function}(self, *args):\n")
                file.write(f"\t\treturn self.process_function('{function}', *args)\n\n")
                    
            file.write(f"\tdef process_function(self, function, *args):\n")
            if stub_type == "client":  
                file.write(f"\t\tserialized_message = self.codec.serialize_function(function, *args)\n")
                file.write(f"\t\tself.client_socket.send(serialized_message)\n")
                file.write(f"\t\tresponse = ''\n")
                file.write(f"\t\twhile True:\n")
                file.write(f"\t\t\tresponse = self.client_socket.recv(1024)\n")
                file.write(f"\t\t\tif not response:\n")
                file.write(f"\t\t\t\tcontinue\n")
                file.write(f"\t\t\telse:\n")
                file.write(f"\t\t\t\tbreak\n")
                file.write(f"\t\toperation_result = self.codec.desserialize_result(response)\n")
                file.write(f"\t\treturn operation_result\n")
                file.close
            else:
                file.write(f"\t\tmethod = getattr(self.service, function)\n")
                file.write(f"\t\tresult = method(*args)\n")
                file.write(f"\t\tprint('Resultado da Operacao: ', result)\n")
                file.write(f"\t\treturn result\n\n")
                file.write(f"\tdef process_message(self, message):\n")
                file.write(f"\t\tfunction_name, args = self.codec.desserialize_function(message)\n")
                file.write(f"\t\tprint('Mensagem Desserializada:' , function_name, args)\n")
                file.write(f"\t\tif not hasattr(self, function_name):\n")
                file.write(f"\t\t\tprint('Metodo' ,function_name, 'nao encontrado')\n")
                file.write(f"\t\telse:\n")
                file.write(f"\t\t\tmethod = getattr(self, function_name)\n")
                file.write(f"\t\t\tresult = method(*args)\n")
                file.write(f"\t\t\treturn self.codec.serialize_result(result)\n")
        
                file.close 
            
    def generate_stub(self, service_name, stub_type):
        service_code = self.read_service(service_name)
        functions, service_class = self.select_functions(service_code)
        self.write_stub(functions, service_class, stub_type, service_name)