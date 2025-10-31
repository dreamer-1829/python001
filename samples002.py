import abc 
from abc import ABC, abstractmethod 
  
class M(ABC): 
    def rk(self): 
        print("Abstract Base Class")
        print("Concrete Method in ABC") 
  
class N(M): 
    def rk(self): 
        super().rk() 
        print("subclass ") 
        print("Concrete Method in subclass")
  
r = N() 
r.rk() 
