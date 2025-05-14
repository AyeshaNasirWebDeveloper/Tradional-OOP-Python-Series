# Assignment: 4

# Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) that allows changing the bank name. Show that it affects all instances.

class Bank:
    bank_name = "Meezan Bank" # class variable

    # class method
    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name
        print(f"Bank name changed to {cls.bank_name}")

# Create instances
bank1 = Bank()
bank2 = Bank()

# Before change
print("Before change:")
print("Bank1:", bank1.bank_name)
print("Bank2:", bank2.bank_name)

# Change bank name using class method
Bank.change_bank_name("HBL Bank")

# After change
print("\nAfter change:")
print("Bank1:", bank1.bank_name)
print("Bank2:", bank2.bank_name)