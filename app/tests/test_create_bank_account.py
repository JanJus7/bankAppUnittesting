import unittest

from ..Konto import Konto

class TestCreateBankAccount(unittest.TestCase):

    def setUp(self):
        self.imie = "Dariusz"
        self.nazwisko = "Januszewski"
        self.numerPESEL = "04251010644"
        self.promoCode = "PROM_IOI"
        self.pierwsze_konto = Konto(self.imie, self.nazwisko, self.numerPESEL, self.promoCode)

    def test_tworzenie_konta(self):
        self.assertEqual(self.pierwsze_konto.imie, "Dariusz", "Imie nie zostało zapisane!")
        self.assertEqual(self.pierwsze_konto.nazwisko, "Januszewski", "Nazwisko nie zostało zapisane!")
        self.assertEqual(self.pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")
        self.assertEqual(self.pierwsze_konto.numerPESEL, "04251010644", "Pesel nie został zapisany!")
        self.assertRegex(self.pierwsze_konto.numerPESEL, r"^[0-9]{11}$", "Niepoprawny pesel!")
        
    def test_promo(self):    
        rok_urodzenia = int(self.pierwsze_konto.numerPESEL[:2])
        miesiac_urodzenia = int(self.pierwsze_konto.numerPESEL[2:4])

        if miesiac_urodzenia >= 20:
            rok_urodzenia += 2000
            miesiac_urodzenia -= 20
        else:
            rok_urodzenia += 1900
        
        if self.promoCode != None:
            if rok_urodzenia >= 1960:
                self.assertRegex(self.pierwsze_konto.promoCode, r"^PROM\_[A-Z]{3}", "Niepoprawny kod promocyjny!")
                self.pierwsze_konto.saldo += 50
                print(self.pierwsze_konto.saldo)
            else:
                print("jesteś za stary!")
    

    #tutaj proszę dodawać nowe testy