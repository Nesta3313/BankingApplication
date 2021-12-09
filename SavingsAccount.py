from BankAccount import BankAccount


class SavingsAccount(BankAccount):
    def __init__(self, account_number, deposit, balance, withdrawal, interest_rate):
        super().__init__(account_number, deposit, balance, withdrawal)
        self.interest_rate = interest_rate/ 100

    def interest(self):
        if self.balance == 0:
            print("Your balance is $0.00, add some funds to calculate interest")
        else:
            year = int(input("Enter number of years to calculate the interest: "))
            final_amount = self.balance * (1 + self.interest_rate) ** year
            interest = final_amount - self.balance
            print("Your interest is $"+str(round(interest,2)), "after: ", year, "year(s)")


customer_savings = SavingsAccount(account_number=22323455, balance=0, withdrawal=0, deposit=0, interest_rate=2)