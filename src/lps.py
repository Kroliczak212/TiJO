class BankAccount:
    def __init__(self):
        self._balance = 0

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
        else:
            raise Exception("Insufficient funds")

    def get_balance(self):
        return self._balance

class SavingsAccount(BankAccount):
    def __init__(self):
        super().__init__()
        self._min_balance = 100

    def withdraw(self, amount):
        if self._balance - amount >= self._min_balance:
            self._balance -= amount
        else:
            raise Exception("Insufficient funds or minimum balance not maintained")

def perform_transaction(account: BankAccount, deposit_amount, withdraw_amount):
    account.deposit(deposit_amount)
    try:
        account.withdraw(withdraw_amount)
        print(f"Balance after transaction: {account.get_balance()}")
    except Exception as e:
        print(f"Transaction failed: {e}")

# Usage
regular_account = BankAccount()
savings_account = SavingsAccount()

perform_transaction(regular_account, 500, 200)   # Works
perform_transaction(savings_account, 500, 450)   # Transaction failed...
