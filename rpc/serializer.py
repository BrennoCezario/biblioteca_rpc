import pickle

class Serializer:
    def __init__(self):
        pass
    
    def serialize_function(self, function, operand_1, operand_2):
        return pickle.dumps((function, (operand_1, operand_2)))
    
    def serialize_result(self, result):
        return pickle.dumps(("RESULT", result))
    
    def desserialize_function(self, message):
        function_name, args = pickle.loads(message)
        return function_name, args
    
    def desserialize_result(self, message):
        response = pickle.loads(message)
        return response