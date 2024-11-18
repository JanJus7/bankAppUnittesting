import re
from .Account import Account

class CompanyAccount(Account):

    expressFee = 5

    def __init__(self, companyName, nip):
        super().__init__()
        self.companyName = companyName
        if re.match("^[0-9]{10}$", nip):
            self.nip = nip
        else:
            self.nip = "Niepoprawny NIP!"

    def takeLoan(self, amount):
        flag = False
        for i in self.history:
            if i == -1775:
                flag = True
                break
        if flag == True and self.balance >= (2*amount):
            self.balance += amount
            self.history.append(amount)