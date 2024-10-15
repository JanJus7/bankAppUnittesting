class Konto:
    def __init__(self, imie, nazwisko, numerPESEL, promoCode):
        self.imie = imie
        self.nazwisko = nazwisko
        self.saldo = 0
        self.numerPESEL = numerPESEL
        self.promoCode = promoCode