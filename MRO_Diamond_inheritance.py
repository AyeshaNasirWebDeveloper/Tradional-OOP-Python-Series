# Assignment No: 15

# Create four classes:
# A with a method show(),
# B and C that inherit from A and override show(),
# D that inherits from both B and C.
# Create an object of D and call show() to observe MRO.

class A:
    def show(self):
        print("This is a class of A")

class B(A):
    def show(self):
        print("This is a class of B")
        super().show()

class C(A):
    def show(self):
        print("This is a class of C")
        super().show()

class D(B, C):
    def show(self):
        print("This is a class of D")
        super().show()
    
d = D()
d.show()