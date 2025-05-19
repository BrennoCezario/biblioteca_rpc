class DistributedCalculator:
    def __init__(self):
        pass
    
    def add(self, x, y):
        try:
            return x+y    
        except TypeError:
            return "ERRO: Necessário inserir um valor de tipo numérico (Exemplo: int ou float)"

    def sub(self, x, y):
        try:
            return x-y
        except TypeError:
            return "ERRO: Necessário inserir um valor de tipo numérico (Exemplo: int ou float)"

    def multiply(self, x, y):
        try:
            return x*y
        except TypeError:
            return "ERRO: Necessário inserir um valor de tipo numérico (Exemplo: int ou float)"

    def divide(self, x, y):
        try:
            return x/y
        except TypeError:
            return "ERRO: Necessário inserir um valor de tipo numérico (Exemplo: int ou float)"
        except ZeroDivisionError:
            return "ERRO: Não é possível realizar divisão por 0!"