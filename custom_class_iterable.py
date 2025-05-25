# Assignment No: 21

# Create a class Countdown that takes a start number. Implement __iter__() and __next__() to make the object iterable in a for-loop, counting down to 0.

class Countdown:
    def __init__(self, start):
        self.current = start  # Starting number

    def __iter__(self):
        return self  # Returning the iterator object itself

    def __next__(self):
        if self.current < 0:
            raise StopIteration 
        else:
            value = self.current
            self.current -= 1
            return value

countdown = Countdown(5)
for number in countdown:
    print(number)
