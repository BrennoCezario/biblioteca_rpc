import math
class DistributedCalculatorPlus:
    def __init__(self):
        pass
    
    def power(self, x, y):
        try:
            return x**y
        except TypeError:
            return "ERRO: Necessário inserir um valor de tipo numérico (Exemplo: int ou float)"
        
    def sqrt(self, x):
        try:
            return math.sqrt(x)
        except TypeError:
            return "ERRO: Necessário inserir um valor de tipo numérico (Exemplo: int ou float)"