class BankAccount:

    total_balance = 0

    def __init__(self,amount):
        self.amount = amount

        BankAccount.total_balance += amount

amount1,amount2 = map(int,input().split())

acc1 = BankAccount(amount1)
acc2 = BankAccount(amount2)

print(BankAccount.total_balance)
    