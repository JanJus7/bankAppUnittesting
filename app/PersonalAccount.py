import re
from .Account import Account

class PersonalAccount(Account):

    expressFee = 1

    def __init__(self, name, surname, pesel, promoCode=None):
        self.name = name
        self.surname = surname
        super().__init__()
        self.pesel = pesel
        self.promoCode = promoCode
        #older method. RE should be better :)
        # if promoCode and promoCode.startswith("PROM_"):
        if promoCode and re.match("^PROM_[A-Z]{3}$", promoCode) and self.isYoungEnough():
            self.balance += 50

    def isYoungEnough(self):
        year = int(self.pesel[:2])
        month = int(self.pesel[2:4])

        if 1 <= month <= 12:
            year += 1900  
        elif 21 <= month <= 32:
            year += 2000  

        return year > 1960
    
    def takeLoan(self, amount):
        lastFiveTransactions = self.history[-5:]  
        sumTransactions = sum(lastFiveTransactions)
        
        lastThreeTransactions = self.history[-3:]
        allIncoming = all(transaction > 0 for transaction in lastThreeTransactions)

        if (allIncoming and len(self.history) >= 3) or (sumTransactions > amount and len(self.history) >= 5):
            self.balance += amount
            self.history.append(amount)