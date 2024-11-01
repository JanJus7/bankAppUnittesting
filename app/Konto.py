import re

class Konto:
    def __init__(self, imie, nazwisko, numerPESEL, promoCode=None):
        self.imie = imie
        self.nazwisko = nazwisko
        self.saldo = 0
        self.numerPESEL = numerPESEL
        self.promoCode = promoCode
        #older method. RE should be better :)
        # if promoCode and promoCode.startswith("PROM_"):
        if promoCode and re.match("PROM_[A-Z]{3}", promoCode):
            self.saldo += 50
    # def incomingTransfer(self, kwota):
    #     self.saldo += kwota


def x(a, b):
    a = 7
    b = 2
    print(a+b)