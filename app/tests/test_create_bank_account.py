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

