class Blabla:
    def __init__(self,a,b):
        self.a = a
        self.b = b
        
    def __str__(self) -> str:
        return f"{self.a}/{self.b}"
    
    def __mul__(self, other):
        if isinstance(other, Blabla):
            return Blabla(self.a*other.a, self.b*other.b)
        
        
    def __add__(self,other):
        if isinstance(other, Blabla):
            return Blabla(self.a*other.b+other.a*self.b, self.b*other.b)

