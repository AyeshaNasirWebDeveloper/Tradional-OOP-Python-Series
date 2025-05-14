# Assignment: 3

# Create a class Car with a public variable brand and a public method start(). Instantiate the class and access both from outside the class.

class Car:

    def __init__(self, brand):
         self.brand = brand # public variable
    
    def start(self):
        print(f"My {self.brand} car is starting.") #public method
    
# Instantiate the class
my_car =Car("Corolla")

# Accessing public variable
print(f"My Car Brand is {my_car.brand}") 

# Calling public method
my_car.start()  