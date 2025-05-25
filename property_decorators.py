# Assignment No: 18

# Create a class Product with a private attribute _price. Use @property to get the price, @price.setter to update it, and @price.deleter to delete it.

class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        '''Get the price of the product.'''
        return self._price
    
    @price.setter
    def price(self, new_price):
        '''Set a new price for the product.'''
        if new_price < 0:
            raise ValueError("Price cannot be negative.")
        self._price = new_price

    @price.deleter
    def price(self):
        '''Delete the price of the product.'''
        print("Deleting price...")
        del self._price

# Example usage
product = Product(1000)
print(f"Access using getter {product.price}")

product.price = 1500 # Update using setter
print(f"Updated using setter {product.price}")

product.price = -500 # Invalid price (setter will show warning)

del product.price # Delete using deleter