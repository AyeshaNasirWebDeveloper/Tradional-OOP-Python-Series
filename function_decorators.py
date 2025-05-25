# Assignment No: 16

# Write a decorator function log_function_call that prints "Function is being called" before a function executes. Apply it to a function say_hello().

# decorator function
def deco(func):
    def wrapper():
        print("Function is being called")
        return func()
    return wrapper

# applying decorator to the function
@deco
def say_hello():
    print("Hello, World from Ayesha Nasir!")

# calling the decorated function
say_hello()