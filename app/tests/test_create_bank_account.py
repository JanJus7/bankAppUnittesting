import unittest

from ..PersonalAccount import PersonalAccount

class CreateBankAccount(unittest.TestCase):
    name = "Dariusz"
    surname = "Januszewski"
    pesel = "04251010644" 

    def testTworzenieKonta(self):
        firstPersonalAccount = PersonalAccount(self.name, self.surname, self.pesel)
        self.assertEqual(firstPersonalAccount.name, "Dariusz", "Imie nie zostało zapisane!")
        self.assertEqual(firstPersonalAccount.surname, "Januszewski", "Nazwisko nie zostało zapisane!")
        self.assertEqual(firstPersonalAccount.balance, 0, "Saldo nie jest zerowe!")
        self.assertEqual(firstPersonalAccount.pesel, "04251010644", "Pesel nie został zapisany!")
        self.assertRegex(firstPersonalAccount.pesel, r"^[0-9]{11}$", "Niepoprawny pesel!")
        
    def testPromoTrue(self):  
        promoCode = "PROM_ABC"     
        firstPersonalAccount = PersonalAccount(self.name, self.surname, self.pesel, promoCode)
        self.assertEqual(firstPersonalAccount.balance, 50, "Saldo nie jest 50!")
        self.assertRegex(firstPersonalAccount.promoCode, promoCode, "Niepoprawny kod promocyjny!")

    def testPromoDeclined(self):
        promoCode = "PROM_ABC"
        pesel = "04051010644" 
        firstPersonalAccount = PersonalAccount(self.name, self.surname, pesel, promoCode)
        self.assertEqual(firstPersonalAccount.balance, 0, "Saldo nie jest 0")

    def testLoan(self):
        firstPersonalAccount = PersonalAccount(self.name, self.surname, self.pesel)
        firstPersonalAccount.history = [100, 500, 600]
        firstPersonalAccount.takeLoan(500)
        self.assertEqual(firstPersonalAccount.balance, 500)
        self.assertEqual(firstPersonalAccount.history, [100, 500, 600, 500], "historia nie została zaktualizowana")

    def testLoanDeclined(self):
        firstPersonalAccount = PersonalAccount(self.name, self.surname, self.pesel)
        firstPersonalAccount.history = [1, -500, 10]
        firstPersonalAccount.takeLoan(500)
        self.assertEqual(firstPersonalAccount.balance, 0)
        self.assertEqual(firstPersonalAccount.history, [1, -500, 10], "błąd w historii")
