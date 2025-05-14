# # Assignment: 7

# Create a class Employee with:
# a public variable name,
# a protected variable _salary, and
# a private variable __ssn.
# Try accessing all three variables from an object of the class and document what happens.

class Employee:
    def __init__(self, name, salary, ssn):
        self.name =name  # Public variable
        self._salary = salary # Protected variable
        self.__ssn = ssn # Private variable

    def display(self):
        print(self.name, self._salary, self.__ssn)

# Create an instance of Employee
employee = Employee("Ayesha Nasir", 150000, "123-45-6789")
print(employee.name)  # Accessing public variable
print(employee._salary)  # Accessing protected variable
# print(employee.__ssn)  # This will raise an AttributeError
print(employee._Employee__ssn)  # Accessing private variable using name mangling but it is not recommended