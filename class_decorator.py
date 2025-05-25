# Assignment No: 17

# Create a class decorator add_greeting that modifies a class to add a greet() method returning "Hello from Decorator!". Apply it to a class Person.

# class decorator
def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    cls.greet = greet
    return cls

# applying class decorator to the class
@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

person = Person("Ayesha Nasir")
print(f"{person.greet()}\n{person.name}") 