import inspect

#We can add lists together in python


list1 = [1,2,3]
list2 = [4,5,6234,234]

print(list1 + list2)
print(len(list1 + list2))

#But...
#List is an object 
print(type(list1+list2)) #<class 'list'>

#Len, addition etc. are already implemented and we can override it


#Double underscore or Dunder methods

class Person:
    def __init__(self, name):
        self.name = name

    def sayName(self):
        print(self.name)

    def __repr__(self):
        return f"Person({self.name})"

    def __mul__(self, p): # Defines what happens when we multiply object with sth else
        if type(p) is not int:
            raise Exception("Invalid args, must enter int")
        return f"{self}*{p}"
    
    def __call__(self, y):
        print(y)
    
    def __len__(self):
        return len(self.name)

p = Person("Filip")

print(p) # Before __repr__  <__main__.Person object at 0x7f4102de1130>
print(p) # After __repr__  Person(Filip)

#print(p*"vhjv") -> throwa an exception

p("y") #__call__

print(f"len(p) = {len(p)}") # No __len__ -> TypeError: object of type 'Person' has no len()

from queue import Queue

q = Queue()
print(q) # <queue.Queue object at 0x7f4102799400>

# print(inspect.getsource(Queue)) # Getting source code

#We can override python sourcecode

class Queue(Queue): # Extends q
    def __repr__(self):
        return f"Queue({self._qsize()})"
        
    def __add__(self, item):
        self.put(item)

qu = Queue(5)
qu + "aasd"
print(qu)
