#create a method overloading and overriding that the completes a banking system
#The parent class must be trasaction and the child class can be deposit, withdrwal and transfer.
#demonstrate an employer depositing, withdrwaing and transfering funds

# Parent Class
class Transaction:
    def process(self):
        print("Processing transaction...")


# Child Class - Deposit
class Deposit(Transaction):

    # Method Overloading using default parameter
    def process(self, amount=None):
        if amount is None:
            print("No deposit amount provided.")
        else:
            print(f"Deposit successful: UGX {amount}")


# Child Class - Withdrawal
class Withdrawal(Transaction):

    # Method Overriding
    def process(self, amount):
        print(f"Withdrawal successful: UGX {amount}")


# Child Class - Transfer
class Transfer(Transaction):

    # Method Overloading using two possible arguments
    def process(self, amount, recipient=None):
        if recipient is None:
            print(f"Transfer of UGX {amount} initiated.")
        else:
            print(f"Transferred UGX {amount} to {recipient}")


# Employer Account
class Employer:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        d = Deposit()
        d.process(amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            w = Withdrawal()
            w.process(amount)
        else:
            print("Insufficient funds!")

    def transfer(self, amount, recipient):
        if amount <= self.balance:
            self.balance -= amount
            t = Transfer()
            t.process(amount, recipient)
        else:
            print("Insufficient funds!")

    def display_balance(self):
        print(f"Current Balance: UGX {self.balance}")


# Demonstration
employer = Employer("Henry", 1000000)

print("Initial Account Details")
employer.display_balance()

print("\n--- Deposit ---")
employer.deposit(500000)
employer.display_balance()

print("\n--- Withdrawal ---")
employer.withdraw(200000)
employer.display_balance()

print("\n--- Transfer ---")
employer.transfer(300000, "John")
employer.display_balance()