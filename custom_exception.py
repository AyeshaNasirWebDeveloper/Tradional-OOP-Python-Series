# Assignment No: 20

# Create a custom exception InvalidAgeError. Write a function check_age(age) that raises this exception if age < 18. Handle it with try...except.

# Custom exception class
class InvalidAgeError(Exception):
    """Custom exception raised when age is less than 18."""
    pass

# Function to check age
def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be at least 18 to proceed.")
    else:
        print("Access granted. Age is valid.")

# handle the exception
try:
    user_age = int(input("Enter your age: "))
    check_age(user_age)
except InvalidAgeError as e:
    print(f"InvalidAgeError caught: {e}")
except ValueError:
    print("Please enter a valid number.")

