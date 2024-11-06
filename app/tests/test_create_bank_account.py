import unittest
from parameterized import parameterized
from ..PersonalAccount import PersonalAccount

class CreateBankAccount(unittest.TestCase):
    name = "Dariusz"
    surname = "Januszewski"
    pesel = "04251010644" 

    def setUp(self):
        self.firstPersonalAccount = PersonalAccount(self.name, self.surname, self.pesel)

    def testTworzenieKonta(self):
        self.assertEqual(self.firstPersonalAccount.name, "Dariusz", "Imie nie zostało zapisane!")
        self.assertEqual(self.firstPersonalAccount.surname, "Januszewski", "Nazwisko nie zostało zapisane!")
        self.assertEqual(self.firstPersonalAccount.balance, 0, "Saldo nie jest zerowe!")
        self.assertEqual(self.firstPersonalAccount.pesel, "04251010644", "Pesel nie został zapisany!")
        self.assertRegex(self.firstPersonalAccount.pesel, r"^[0-9]{11}$", "Niepoprawny pesel!")
    
    # Not needed anymore beacuse I can do it in parameterized with one def :)
    # def testPromoTrue(self):  
    #     promoCode = "PROM_ABC"     
    #     self.assertEqual(self.firstPersonalAccount.balance, 50, "Saldo nie jest 50!")

    @parameterized.expand([
        ("PROM_ABC", "04051010644", 0),
        ("PROM_123", "04251010644", 0),
        ("NIC", "04251010644", 0),
        ("PROM_abc", "04251010644", 0),
        ("PROM_ABCD", "04251010644", 0),
        ("ProM_CDF", "04251010644", 0),
        ("PROM_ABC", "04251010644", 50),
        ("PROM_FLO", "04251010644", 50),
        ("ASDPROM_ASDAS", "04251010644", 0)
    ])

    def testPromo(self, code, pesel, balance):
        promoCode = code
        promoPersonalAccount = PersonalAccount(self.name, self.surname, pesel, promoCode)
        self.assertEqual(promoPersonalAccount.balance, balance, "Saldo nie jest 0")

    @parameterized.expand([
        ([100, 500, 600], 500, 500, [100, 500, 600, 500]),
        ([1, -500, 10], 500, 0, [1, -500, 10]),
        ([100, 200, -99], 200, 0, [100, 200, -99]),
        ([100, 200], 200, 0, [100, 200]),
        ([10000, -1, 5000, 100000], 10, 0, [10000, -1, 5000, 100000]),
        ([600, 500, 200, -100, -200, -100], 200, 200, [600, 500, 200, -100, -200, -100, 200]),
        ([-100, -200, -400, -100, 200], 700, 0, [-100, -200, -400, -100, 200])
    ])


    def testLoan(self, history, loanAmount, expeactedBalance, expectedHistory):
        self.firstPersonalAccount.history = history
        self.firstPersonalAccount.takeLoan(loanAmount)
        self.assertEqual(self.firstPersonalAccount.balance, expeactedBalance)
        self.assertEqual(self.firstPersonalAccount.history, expectedHistory, "historia nie została zaktualizowana")
