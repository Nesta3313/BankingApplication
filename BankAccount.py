class BankAccount:
    def __init__(self, account_number, withdrawal,  deposit = 0.00, balance = 0.00):
        self.account_number = account_number
        self.balance = balance
        self.deposit = deposit
        self.withdrawal = withdrawal


    def get_deposit(self):
        deposit_amount = float(input("Enter deposit amount: "))
        self.deposit = deposit_amount
        self.balance += self.deposit
        print("You have deposited: "+ str(deposit_amount))

    def get_withdrawal(self):
        withdraw_amount = float(input("How much are you withdrawing today?; "))
        if withdraw_amount > self.balance or self.balance == 0:
            print("You have insufficient funds, deposit some funds to withdraw")
        else:
            self.withdrawal = withdraw_amount
            print("You have withdrawn " + str(self.withdrawal))
            self.balance = self.balance - withdraw_amount



    def get_balance(self):
        print("Your balance is: " +"$"+str(self.balance))





















