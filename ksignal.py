class ksignal():
    def __init__(self):
        self.functions = []
    
    def connect(self, functions):
        if type(functions) == list:
            indices = []
            full = False
            
            for function in functions:
                if not full:
                    for index,val in enumerate(self.functions):
                        if val == None:
                            self.functions[index] = function
                            indices.append(index)
                            break
                    else:
                        full = True
                        self.functions.append(function)
                        indices.append(len(self.functions) - 1)
                else:
                    self.functions.append(function)
                    indices.append(len(self.functions) - 1)
            
            return indices
                
        else:
            for index,val in enumerate(self.functions):
                if val == None:
                    self.functions[index] = functions
                    return index

            self.functions.append(functions)
            return len(self.functions) - 1
    
    def disconnect(self, index):
        if type(index) == list:
            for index in index:
                if index < len(self.functions):
                    self.functions[index] = None
        else:
            if index < len(self.functions):
                self.functions[index] = None
    
    def reset(self):
        self.functions = []

    def fire(self, *args):
        for function in self.functions:
            if function != None:
                function(*args)