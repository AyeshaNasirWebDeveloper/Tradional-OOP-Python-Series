# Assignment 2

# Create a class Counter that keeps track of how many objects have been created. Use a class variable and a class method with cls to manage and display the count.

class Counter:
    count = 0

    def __init__(self):
        Counter.count_tracker()

    @classmethod
    def count_tracker(cls):
        cls.count += 1
        return cls.count

object1 = Counter()
object2 = Counter()
object3 = Counter()
object4 = Counter()
object5 = Counter()

print(f"Object Total Count = {Counter.count}") 