# Functions are object - we can define them in another func and pass it around
# Then lets say we want to pass function in func and execute it

def func(f):
    def func_obj(*args,**kwargs): # Like this we can pass any number of arguments without knowing apriori
        print("Started...")
        return_value = f(*args,**kwargs) # print(f)
        print("Ended...")

        return return_value
    
    return func_obj

# func_obj = func("string")
# func_obj()

@func
def func2():
    print("func2")

@func
def func3():
    print("func3")

# Timing

import time

def timer(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        return_value = func(*args,**kwargs)
        total = time.time() - start
        print(f"Time: {total}")
        return return_value
    
    return wrapper

@timer
def test():
    for _ in range(10000):
        pass


