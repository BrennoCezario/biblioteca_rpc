class DistributedCalculator:
    def __init__(self):
        pass
    
    def add(x,y):
        try:
            return x+y    
        except TypeError:
            return "ERRO: Necessário inserir um valor de tipo numérico (Exemplo: int ou float)"

    def sub(x,y):
        try:
            return x-y
        except TypeError:
            return "ERRO: Necessário inserir um valor de tipo numérico (Exemplo: int ou float)"

    def multiply(x,y):
        try:
            return x*y
        except TypeError:
            return "ERRO: Necessário inserir um valor de tipo numérico (Exemplo: int ou float)"

    def divide(x,y):
        try:
            return x/y
        except TypeError:
            return "ERRO: Necessário inserir um valor de tipo numérico (Exemplo: int ou float)"
        except ZeroDivisionError:
            return "ERRO: Necessário inserir valores do tipo integer ou float!"
        
    print("Resultado da divisao:", divide("1",5))