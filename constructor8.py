"""
Create a BankAccount calss with constructor for acc_holder and balance
Add a method deposit(amount) to increase balance
Add a method withdraw(amount) to decrease balance if sufficient
Make two accounts, deposit money in first and withdraw fron second then print both balances
"""


class BankAccount:
    def __init__(self,acc_holder,balance):
        self.acc_holder = acc_holder
        self.balance    = balance

    def deposit(self,amount):
        self.balance += amount
        return self.balance
    
    def withdraw(self,amount):
        if(amount < 0):
            print("Invalid")
            return self.balance

        if (self.balance < amount):
            print("Insufficient Amount, Cannot withdraw")
            return self.balance
        else:
            self.balance -= amount
            return self.balance


holder1 =  BankAccount("Omkar",50000)

holder1.deposit(5000)
print("Current Balance :",holder1.balance)


holder2 =  BankAccount("Rohit",50000)

holder2.withdraw(5000)
print("Current Balance :",holder2.balance)

