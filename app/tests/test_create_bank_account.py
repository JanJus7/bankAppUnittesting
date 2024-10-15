import unittest

from ..Konto import Konto

class TestCreateBankAccount(unittest.TestCase):

    def test_tworzenie_konta(self):
        imie = "Dariusz"
        nazwisko = "Januszewski"
        numerPESEL = "04251010644"
        promoCode = "PROM_IOI"
        pierwsze_konto = Konto(imie, nazwisko, numerPESEL, promoCode)
        self.assertEqual(pierwsze_konto.imie, "Dariusz", "Imie nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.nazwisko, "Januszewski", "Nazwisko nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")
        self.assertEqual(pierwsze_konto.numerPESEL, "04251010644", "Pesel nie został zapisany!")
        self.assertRegex(pierwsze_konto.numerPESEL, r"^[0-9]{11}$", "Niepoprawny pesel!")
        
        rok_urodzenia = int(pierwsze_konto.numerPESEL[:2])
        miesiac_urodzenia = int(pierwsze_konto.numerPESEL[2:4])

        if miesiac_urodzenia >= 20:
            rok_urodzenia += 2000
            miesiac_urodzenia -= 20
        else:
            rok_urodzenia += 1900
        
        if promoCode != None:
            if rok_urodzenia >= 1960:
                self.assertRegex(pierwsze_konto.promoCode, r"^PROM\_[A-Z]{3}", "Niepoprawny kod promocyjny!")
                pierwsze_konto.saldo += 50
                print(pierwsze_konto.saldo)
            else:
                print("jesteś za stary!")



    #tutaj proszę dodawać nowe testy