class ATM:
    def __init__(self, balance):
        self.balance = balance   # initial balance

    def check_balance(self):
        print("Your Balance is:", self.balance)

    def deposit(self, amount):
        self.balance += amount
        print(amount, "deposit ho gaya")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(amount, "withdraw ho gaya")
        else:
            print("Insufficient balance ❌")


# object create
atm = ATM(1000)

# operations
atm.check_balance()
atm.deposit(500)
atm.withdraw(300)
atm.check_balance()