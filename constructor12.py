"""
Create a Python class BankAccount that simulates a simple bank system.

Constructor (__init__) should take: acc_holder (string) → account holder name, balance (integer) → initial balance

Methods:
deposit(amount) → Adds amount to balance and returns the new balance
withdraw(amount) → Subtracts amount if balance is sufficient, else prints "Insufficient balance" and balance remains same
display() → Prints: Account Holder: <acc_holder>, Balance: <balance>

Extra Challenge:
Add a class variable bank_name = "MyBank"
In display(), also print the bank name: Account Holder: <acc_holder>, Balance: <balance>, Bank: MyBank

Tasks:
Create 2 accounts:
Omkar → 50,000
Rohit → 30,000

Deposit 5,000 in Omkar’s account
Withdraw 10,000 from Rohit’s account
Call display() for both accounts
"""

class BankAccount:
    bank_name = "MyBank"

    def __init__(self,acc_holder,balance):
        self.acc_holder = acc_holder
        self.balance    = balance
    
    def deposit(self,amount):
        self.balance += amount
        return self.balance
    
    def withdraw(self,amount):
        if (self.balance < amount):
            print("Insufficient Balance")
            return self.balance
        
        if (amount < 0):
            print ("Invalid Amount")
            return self.balance
        else:
            self.balance -= amount
            return self.balance
        
    def display(self):
        print("Account Holder :",self.acc_holder,"Balance :",self.balance, "Bank :",BankAccount.bank_name, end=" ")

cust1 = BankAccount("Omkar",50000)
cust2 = BankAccount("Rohit",30000)

cust1.deposit(5000)
cust2.withdraw(10000)

cust1.display()
print("\n")
cust2.display()