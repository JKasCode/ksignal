class ksignal():
    def __init__(self):
        self.functions = []
    
    def connect(self, f):
        if type(f) == list:
            indices = []
            full = False
            
            for a in f:
                if not full:
                    for i,val in enumerate(self.functions):
                        if val == None:
                            self.functions[i] = a
                            indices.append(i)
                            break
                    else:
                        full = True
                        self.functions.append(a)
                        indices.append(len(self.functions) - 1)
                else:
                    self.functions.append(a)
                    indices.append(len(self.functions) - 1)
            
            return indices
                
        else:
            for i,val in enumerate(self.functions):
                if val == None:
                    self.functions[i] = f
                    return i

            self.functions.append(f)
            return len(self.functions) - 1
    
    def disconnect(self, i):
        if type(i) == list:
            for index in i:
                if index < len(self.functions):
                    self.functions[index] = None
        else:
            if i < len(self.functions):
                self.functions[i] = None
    
    def disconnect_all(self):
        self.functions = []
    
    def get_connected(self):
        return self.functions

    def fire(self, *args):
        for f in self.functions:
            if f != None:
                f(*args)