from BankAccount import BankAccount


class SavingsAccount(BankAccount):
    def __init__(self, interest_rate, account_number, deposit, balance, withdrawal):
        super().__init__(account_number, deposit, balance, withdrawal)
        self.interest_rate = interest_rate

    def interest(self):
        year = 1
        final_amount = self.balance * (1 + self.interest_rate) ** year

customer = SavingsAccount(account_number=22323455, balance=0, withdrawal=0, deposit=0, interest_rate=0.05)