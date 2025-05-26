import os
from rpc.rpc_client import Client

def run_math_example(client, service_name):
    
    client.start_service_search(service_name)
    
    while True:
        try:
            print("\nOperações disponíveis:")
            print("1. Soma")
            print("2. Subtração")
            print("3. Multiplicação")
            print("4. Divisão")
            print("0. Sair")
            
            choice = int(input("Escolha uma operação: "))
            
            if choice > 4 and choice < 0:
                continue

        except ValueError:
            print("\nDigite apenas valores de 0 a 4\nTente Novamente!")
            continue
        
        try:
            if choice == 0:
                break

            x = float(input("Primeiro número: "))
            y = float(input("Segundo número: "))

        except ValueError:
            print("\nDigite apenas valores numéricos(ex: int ou float)\nTente Novamente!")
            continue

        match choice: 
            case 1:
                print(f"Resultado: {client.service_stub.add(x, y)}")
            case 2:
                print(f"Resultado: {client.service_stub.sub(x, y)}")
            case 3:
                print(f"Resultado: {client.service_stub.multiply(x, y)}")
            case 4:
                print(f"Resultado: {client.service_stub.divide(x, y)}")
                
def run_math_plus_example(client, service_name):
    
    client.start_service_search(service_name)
    
    while True:
        try:
            print("\nOperações disponíveis:")
            print("1. Raíz quadrada")
            print("2. Potência")
            print("0. Sair")
            
            choice = int(input("Escolha uma operação: "))
            
            if choice > 2 and choice < 0:
                continue

        except ValueError:
            print("\nDigite apenas valores de 0 a 2\nTente Novamente!")
            continue
        
        try:
            if choice == 0:
                break
            
            x = float(input("Primeiro número: "))
            y=0
            if choice == 2:
                y = float(input("Segundo número: "))

        except ValueError:
            print("\nDigite apenas valores numéricos(ex: int ou float)\nTente Novamente!")
            continue

        match choice: 
            case 1:
                print(f"Resultado: {client.service_stub.sqrt(x)}")
            case 2:
                print(f"Resultado: {client.service_stub.power(x, y)}")
                
if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== Cliente de Exemplo RPC ===")
 
    client = Client()
    try:
        while True:
            service_name = input("\nDigite o serviço desejado (ex: math): ")
            
            if service_name.lower() == "math":
                run_math_example(client, service_name)
                print("\nDeseja continuar a busca?")
                print("1. Sim")
                print("2. Não")
                
                choice = int(input("Opção Escolhida: "))

                if choice == 1:
                    continue
                elif choice == 2:
                    break
                break
            elif service_name.lower() == "math_plus":
                run_math_plus_example(client, service_name)
                print("\nDeseja continuar a busca?")
                print("1. Sim")
                print("2. Não")
                
                choice = int(input("Opção Escolhida: "))

                if choice == 1:
                    continue
                elif choice == 2:
                    break
                break
            else:
                print(f"Serviço {service_name} não suportado neste exemplo")
                print("\nDeseja continuar a busca?")
                print("1. Sim")
                print("2. Não")
                
                choice = int(input("Opção Escolhida: "))

                if choice == 1:
                    continue
                elif choice == 2:
                    break
                else:
                    print("Não foi possível processar essa reposta, então a busca será finalizada.")
                    break  
    except KeyboardInterrupt:
        print("\nEncerrando client...")