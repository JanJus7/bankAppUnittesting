import re
from .Konto import Konto

class PersonalAccount(Konto):

    expressFee = 1

    def __init__(self, imie, nazwisko, numerPESEL, promoCode=None):
        self.imie = imie
        self.nazwisko = nazwisko
        super().__init__()
        self.numerPESEL = numerPESEL
        self.promoCode = promoCode
        #older method. RE should be better :)
        # if promoCode and promoCode.startswith("PROM_"):
        if promoCode and re.match("PROM_[A-Z]{3}", promoCode) and self.isYoungEnough():
            self.saldo += 50

    def isYoungEnough(self):
        year = int(self.numerPESEL[:2])
        month = int(self.numerPESEL[2:4])

        if 1 <= month <= 12:
            year += 1900  
        elif 21 <= month <= 32:
            year += 2000  

        return year > 1960
    
    def takeLoan(self, amount):
        last_transactions = self.historia[-5:]  
        sumTransactions = sum(last_transactions)
        
        last_three_transactions = self.historia[-3:]
        all_incoming = all(transaction > 0 for transaction in last_three_transactions)
    
        if all_incoming or sumTransactions > amount:
            self.saldo += amount
            self.historia.append(amount)