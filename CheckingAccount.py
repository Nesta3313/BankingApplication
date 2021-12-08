from BankAccount import BankAccount

class CheckingAccount(BankAccount):
    minimum_balance = 50
    def __init__(self, account_number, balance, deposit, withdrawal, fees, minimum_balance = 50):
        super().__init__(account_number, deposit, balance, withdrawal)
        self.fees = fees
        self.minimum_balance = minimum_balance

    def deduct_fee(self):
        self.balance  = self.balance - self.fees



    def check_minimum_balance(self):
        if self.balance < self.minimum_balance:
            return "Your account balance is below $50"

customer = CheckingAccount(account_number=234333, balance=0, deposit=0, fees=5, withdrawal=0)