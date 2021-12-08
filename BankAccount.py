class BankAccount:
    def __init__(self, account_number, deposit = 0, balance = 0, withdrawal = 0):
        self.account_number = account_number
        self.balance = balance
        self.deposit = deposit
        self.withdrawal = withdrawal


    def get_deposit(self):
        self.deposit = float(input("Enter deposit amount: "))
        print("You have deposited: "+ str(self.deposit))

    def get_withdrawal(self):
        self.withdrawal = float(input("How much are you withdrawing today?; "))
        print("You have withdrawn " + str(self.withdrawal))

    def get_balance(self):
        print("Your balance is: " + str(self.balance))





















