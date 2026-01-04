class BankAccount:
    __no = ""
    __balance = 0

    def __init__(self, no):
        self.__no = 0
    
    @property
    def balance(self):
        return self.__balance
    
    @property
    def no(self):
        return self.__no
    
    def topup(self, topup_amount):
        self.__balance += topup_amount

    def cashout(self, cashout_amount):
        if cashout_amount > self.__balance:
            raise ValueError("Not enough balance")
        self.__balance -= cashout_amount

account1 = BankAccount("eko")
print(account1.no)
print(account1.balance)

account1.topup(10000)
print(account1.balance)

account1.cashout(5000)
print(account1.balance)


# account1.cashout(1000000) # error