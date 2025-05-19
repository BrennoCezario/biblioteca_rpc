import os
from rpc.rpc_client import Client

def run_math_example(client, service_name):
    
    client.start_service_search(service_name)
    
    while True:
        print("\nOperações disponíveis:")
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("0. Sair")
        
        choice = input("Escolha uma operação: ")
        
        if choice == "0":
            break
        
        x = float(input("Primeiro número: "))
        y = float(input("Segundo número: "))
        match choice: 
            case '1':
                print(f"Resultado: {client.math_stub.add(x, y)}")
            case '2':
                print(f"Resultado: {client.math_stub.sub(x, y)}")
            case '3':
                print(f"Resultado: {client.math_stub.multiply(x, y)}")
            case '4':
                print(f"Resultado: {client.math_stub.divide(x, y)}")

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== Cliente de Exemplo RPC ===")
 
    client = Client()
    
    service_name = input("\nDigite o serviço desejado (ex: math): ")
    
    if service_name.lower() == "math":
        run_math_example(client, service_name)
    else:
        print(f"Serviço {service_name} não suportado neste exemplo")