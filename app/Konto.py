class Konto:
    def __init__(self, imie, nazwisko, numerPESEL, promoCode=None):
        self.imie = imie
        self.nazwisko = nazwisko
        self.saldo = 0
        self.numerPESEL = numerPESEL
        self.promoCode = promoCode
        if promoCode and promoCode.startswith("PROM_"):
            self.saldo += 50
    # def incomingTransfer(self, kwota):
    #     self.saldo += kwota
