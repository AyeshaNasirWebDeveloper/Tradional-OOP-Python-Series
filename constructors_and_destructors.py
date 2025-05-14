# Assignment: 6

# Create a class Logger that prints a message when an object is created (constructor) and another message when it is destroyed (destructor).

class Logger:

    def __init__(self):
        print('Object created!')

    def __del__(self):
        print('Object destroyed!')

# Create an object of the Logger class
log_obj = Logger()


