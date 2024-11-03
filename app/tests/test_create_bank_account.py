import unittest

from ..Konto import Konto

class CreateBankAccount(unittest.TestCase):

    def setUp(self):
        self.imie = "Dariusz"
        self.nazwisko = "Januszewski"

    def testTworzenieKonta(self):
        numerPESEL = "04251010644"
        pierwsze_konto = Konto(self.imie, self.nazwisko, numerPESEL)
        self.assertEqual(pierwsze_konto.imie, "Dariusz", "Imie nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.nazwisko, "Januszewski", "Nazwisko nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")
        self.assertEqual(pierwsze_konto.numerPESEL, "04251010644", "Pesel nie został zapisany!")
        self.assertRegex(pierwsze_konto.numerPESEL, r"^[0-9]{11}$", "Niepoprawny pesel!")
        
    def testPromoTrue(self):  
        promoCode = "PROM_ABC"   
        numerPESEL = "04251010644"  
        pierwsze_konto = Konto(self.imie, self.nazwisko, numerPESEL, promoCode)
        self.assertEqual(pierwsze_konto.saldo, 50, "Saldo nie jest 50!")
        self.assertRegex(pierwsze_konto.promoCode, promoCode, "Niepoprawny kod promocyjny!")

    def testPromoDeclined(self):
        promoCode = "PROM_ABC" 
        numerPESEL = "04051010644" 
        pierwsze_konto = Konto(self.imie, self.nazwisko, numerPESEL, promoCode)
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest 0")

# class TestTransfers(CreateBankAccount):
#     def testIncomes(self):
#         incomingTransfer()
#         self.assertEqual(self.pierwsze_konto.saldo, 50, "Nie otrzymałeś jeszcze żadnego przelewu")