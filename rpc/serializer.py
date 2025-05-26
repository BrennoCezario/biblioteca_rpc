import pickle

class Serializer:
    def __init__(self):
        pass
    
    def serialize_function(self, function, *args):
        return pickle.dumps((function, (args)))
    
    def serialize_result(self, result):
        return pickle.dumps((result))
    
    def desserialize_function(self, message):
        function_name, args = pickle.loads(message)
        return function_name, args
    
    def desserialize_result(self, message):
        response = pickle.loads(message)
        return response