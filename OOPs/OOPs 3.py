#BankAccount Class with Deposit, Withdrawal, and Transaction History

class BankAccount:
    def __init__(self, account_number, name, balance, date_of_opening):
        self.account_number = account_number
        self.name = name
        self.balance = balance
        self.date_of_opening = date_of_opening
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f'Deposited: {amount}. New balance: {self.balance}')
        else:
            print('Deposit amount must be positive.')
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f'Withdrawn: {amount}. New balance: {self.balance}')
        else:
            print('Withdrawal amount must be valid.')
        
    def check_balance(self):
        print(f'Current balance: {self.balance}')

cust1 = BankAccount('123456789', 'Pulkit', 15000, '2023-01-01')
cust2 = BankAccount('987654321', 'Ayush', 12000, '2024-01-06')

cust1.deposit(5000)
cust1.check_balance()