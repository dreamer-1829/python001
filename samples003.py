import abc
from abc import ABC, abstractmethod
class addition(ABC):
    first = 0
    second = 0
    Answer=0
def minion(self,a ,b):
  self.first=a
  self.second=b
def ziya(self):
  print("First number:",self.first)
  print("Second number:",self.second)   
  print("The sum is:",self.Answer)
def calculate(self):
  self.Answer=self.first + self.second
  obj=addition(2000,3000)
  obj.calculate()
  obj.ziya()