# Class in Python is an object 
# We have a higher level class that crates class object for us

# class Class:
#     pass

class SuperClass:
    def __init__(self):
         self.a = "hardcoded a"

def method1(self,x,y):
    return x + y

Class = type('Class', (SuperClass,), {"x":5, "method1":method1}) # type('NameOfAClass', (extends), {attributes})

print(Class) # <class '__main__.Class'>

print(type(Class)) # <class 'type'> type is a metaclass

obj = Class()

print(obj.x) # 5
print(obj.a)
print(obj.method1(1,2))

class Meta(type):
    def __new__(self,class_name,bases,attrs): # Gets called right before __init__
        print(attrs)

        return type(class_name,bases,attrs)

