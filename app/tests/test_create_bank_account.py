import unittest

from ..PersonalAccount import PersonalAccount

class CreateBankAccount(unittest.TestCase):

    def setUp(self):
        self.imie = "Dariusz"
        self.nazwisko = "Januszewski"
        self.numerPESEL = "04251010644" 

    def testTworzenieKonta(self):
        pierwsze_konto = PersonalAccount(self.imie, self.nazwisko, self.numerPESEL)
        self.assertEqual(pierwsze_konto.imie, "Dariusz", "Imie nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.nazwisko, "Januszewski", "Nazwisko nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")
        self.assertEqual(pierwsze_konto.numerPESEL, "04251010644", "Pesel nie został zapisany!")
        self.assertRegex(pierwsze_konto.numerPESEL, r"^[0-9]{11}$", "Niepoprawny pesel!")
        
    def testPromoTrue(self):  
        promoCode = "PROM_ABC"     
        pierwsze_konto = PersonalAccount(self.imie, self.nazwisko, self.numerPESEL, promoCode)
        self.assertEqual(pierwsze_konto.saldo, 50, "Saldo nie jest 50!")
        self.assertRegex(pierwsze_konto.promoCode, promoCode, "Niepoprawny kod promocyjny!")

    def testPromoDeclined(self):
        promoCode = "PROM_ABC" 
        numerPESEL = "04051010644" 
        pierwsze_konto = PersonalAccount(self.imie, self.nazwisko, numerPESEL, promoCode)
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest 0")

    def testLoan(self):
        konto = PersonalAccount(self.imie, self.nazwisko, self.numerPESEL)
        konto.historia = [100, 500, 600]
        konto.takeLoan(500)
        self.assertEqual(konto.saldo, 500)
        self.assertEqual(konto.historia, [100, 500, 600, 500], "historia nie została zaktualizowana")

    def testLoanDeclined(self):
        konto = PersonalAccount(self.imie, self.nazwisko, self.numerPESEL)
        konto.historia = [1, -500, 10]
        konto.takeLoan(500)
        self.assertEqual(konto.saldo, 0)
        self.assertEqual(konto.historia, [1, -500, 10], "błąd w historii")