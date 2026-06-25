#polymorphism
class Calculator:
    def add(self, a,b):
        if isinstance(a,int) and isinstance(b,int):
            return a+b
        elif isinstance(a,float) or isinstance(b, float):
            return float(a) +float(b)
        elif isinstance(a,str) or isinstance(b, str):
            return str(a)+ str(b)
        

#method overriding
'''
-the method signature (name and parameter) must match
-super() allow calling the parent method
-Overriding enable dynamic behaviours at runtime
'''

#real world example: Bank Account

class BankAccount:
    def calculate_interest (self, balance, rate):
        return balance *rate/100
    def get_account_type(self):
        return 'Generic Bank Account'
    
class SavingAccount(BankAccount):
    def calculate_interest(self, balance, rate):
        monthly_rate =rate/12/100
        return balance *((1+monthly_rate)**12-1)
    
    def get_account_type(self):
        return 'Saving Account'
           
