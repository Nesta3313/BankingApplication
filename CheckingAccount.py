from BankAccount import BankAccount

class CheckingAccount(BankAccount):

    def __init__(self, account_number, balance, deposit, withdrawal, fees, minimum_balance = 50):
        super().__init__(account_number, deposit, balance, withdrawal)
        self.fees = fees
        self.minimum_balance = minimum_balance

    def deduct_fee(self):
        self.balance  = self.balance - self.fees

    def check_minimum_balance(self):
        self.get_balance()
        if self.balance< self.minimum_balance:
            print("Your account balance is below $50")
        elif self.balance == self.minimum_balance:
            print("Your balance is $"+ str(self.balance )+ ", this is the minimum balance")
        else:
            print("Your balance is $"+ str(self.balance )+ ", it is above minimum balance")

customer = CheckingAccount(account_number=234333, balance=0, deposit=0, fees=5, withdrawal=0)