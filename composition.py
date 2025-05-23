# Assignment No: 13

# Create a class Engine and a class Car. Use composition by passing an Engine object to the Car class during initialization. Access a method of the Engine class via the Car class.

class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower
    
    def start(self):
        return print(f"Engine with {self.horsepower} horsepower started.")

    def stop(self):
        return print("Engine stopped.")
    
class Car:
    def __init__(self, make, model, engine):
        self.make = make
        self.model = model
        self.engine = engine
    
    def start(self):
        print(f"{self.make} {self.model} is starting.")
        self.engine.start()
    
    def stop(self):
        print(f"{self.make} {self.model} is stopping.")
        self.engine.stop()

engine = Engine(150)
car = Car("Toyota", "Camry", engine)
car.start()
car.stop()