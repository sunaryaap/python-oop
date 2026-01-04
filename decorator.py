class Matematika:

    @staticmethod
    def tambah(a, b):
        return a + b
    
print(Matematika.tambah(1, 2))

class BankAccount:
    no = ""
    balance = 0
    active = True

    def __init__(self, no, balance=0):
        self.no = no
        self.balance = balance
    
    @classmethod
    def disabled(cls, no, balance=0):
        result = cls(no, balance)
        result.active = False
        return result

bank_account1 = BankAccount("1234567890", 100000)
bank_account1.balance = -1000
print(f"{bank_account1.no}, {bank_account1.balance}, {bank_account1.active}")

bank_account2 = BankAccount.disabled("1234567890", 100000)
print(f"{bank_account2.no}, {bank_account2.balance}, {bank_account2.active}")


# class Category:
#     _name = ""

#     def set_name(self, name):
#         if name == "":
#             raise ValueError("Name cannot be empty")
#         self._name = name
    
#     def get_name(self):
#         return self._name
    
# category1 = Category()
# category1.set_name("Gadget")
# print(category1.get_name())

class Category:
    __name = ""

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        if name == "":
            raise ValueError("Name cannot be empty")
        self.__name = name

category1 = Category()
category1.name = "Laptop"
print(category1.name)
print(category1.name)