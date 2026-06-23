#data hiding
#real world bank account (balance, deposit)

class BankAccount:
    def __init__(self):
        self.__balance = 1000000  # private attribute

    def deposit(self, amount):
        self.__balance += amount

    def show_balance(self):
        return self.__balance

account = BankAccount()
account.deposit(50000)
print(account.show_balance())