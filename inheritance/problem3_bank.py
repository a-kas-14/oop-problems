class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

    # Move money from this account to another account
    def transfer(self, destination, amount):
        if amount > self.balance:
            return False          # not enough money
        self.balance -= amount
        destination.deposit(amount)
        return True


class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance=0, interest_rate=0.0):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate   # 0.05 means 5%

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        return interest

    def check_balance(self):
        return self.balance


if __name__ == "__main__":
    checking = BankAccount("A001", 1000)
    savings = SavingsAccount("S001", 500, 0.05)

    checking.deposit(200)
    print("After deposit of 200:", checking.balance)          # 1200

    checking.withdraw(100)
    print("After withdraw of 100:", checking.balance)         # 1100

    print("Transfer 300 to savings:", checking.transfer(savings, 300))   # True
    print("Checking balance:", checking.balance)              # 800
    print("Savings balance:", savings.check_balance())        # 800

    print("Transfer 5000 to savings:", checking.transfer(savings, 5000)) # False

    savings.add_interest()
    print("Savings after 5% interest:", savings.check_balance())  # 840.0

