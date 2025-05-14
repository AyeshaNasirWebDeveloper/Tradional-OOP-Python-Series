# Create a class Student with attributes name and marks. Use the self keyword to initialize these values via a constructor. Add a method display() that prints student details.

class Student:
    # Constructor / Dunder method
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    # Method 
    def display(self):
        print(f"Name: {self.name}, \nMarks: {self.marks}")

Student1 = Student("Ayesha Nasir", 95)
Student1.display()

Student2 = Student("Muhammad Nasir", 97)
Student2.display()

