# Assignment No: 14

# Create a class Department and a class Employee. Use aggregation by having a Department object store a reference to an Employee object that exists independently of it.

class Department:
    def __init__(self, name):
        self.name = name
        
class Employee:
    def __init__(self, name, age):
            self.name = name
            self.age = age
            
    def display(self):
            print(f"Employee Name: {self.name}, Age: {self.age}")

employee1 = Employee("Muhammad", 20)
employee2 = Employee("Ahmed", 25)
employee3 = Employee("Ali", 30)

department = Department("IT Department")

print("Department:", department.name)
employee1.display()
employee2.display()
employee3.display()