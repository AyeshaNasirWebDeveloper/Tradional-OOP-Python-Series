# Assignment No. 19

# Create a class Multiplier with an __init__() to set a factor. Define a __call__() method that multiplies an input by the factor. Test it with callable() and by calling the object like a function.

class Multiplier:
    def __init__(self):
        self.factor = 20
    
    def __call__(self, value):
        """Multiply the input value by the factor."""
        return value* self.factor
    
# Example usage
multiplier = Multiplier()
print(f"Is multiplier callable? {callable(multiplier)}")  # Check if the object is callable
print(f"Calling multiplier with 5: {multiplier(5)}")  # Call the object like a function