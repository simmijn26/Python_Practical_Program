
# Q23. Class BankAccount

class BankAccount:
    def __init__(self, bal):
        self.balance = bal

    def deposit(self, amt):
        self.balance += amt

    def withdraw(self, amt):
        self.balance -= amt

    def display(self):
        print("Balance:", self.balance)

b = BankAccount(float(input("Enter initial balance: ")))

b.deposit(float(input("Deposit amount: ")))
b.withdraw(float(input("Withdraw amount: ")))
b.display()