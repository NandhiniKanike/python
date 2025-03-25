class InsufficientFundsException(Exception):
    def __init__(self, balance, withdrawal_amount):
        self.balance = balance
        self.withdrawal_amount = withdrawal_amount
        super().__init__(f"Insufficient funds! Available: {balance}, Requested: {withdrawal_amount}")

# Real-Time Use Case
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsException(self.balance, amount)
        self.balance -= amount
        print(f"Withdrawal successful. Remaining balance: {self.balance}")

# Example Usage
try:
    account = BankAccount(balance=1000)
    account.withdraw(1500)
except InsufficientFundsException as e:
    print(e)
finally:
    print("THIS IS THE EXAMPLE FOR EXCEPTION HANDLING")