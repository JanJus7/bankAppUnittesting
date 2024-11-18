import unittest
from parameterized import parameterized
from ..PersonalAccount import PersonalAccount
from ..AccountRegistry import AccountRegistry

class TestRegistry(unittest.TestCase):
    imie = "Dariusz"
    nazwisko = "Januszewski"
    pesel = "676756678"
    pesel66 = "66666666666"
    pesel77 = "77777777777"

    @classmethod
    def setUpClass(cls):
        cls.konto66 = PersonalAccount(cls.imie, cls.nazwisko, cls.pesel66)
        cls.konto77 = PersonalAccount(cls.imie, cls.nazwisko, cls.pesel77)

    def setUp(self):
        AccountRegistry.registry = []
        konto = PersonalAccount(self.imie, self.nazwisko, self.pesel)
        AccountRegistry.addAccount(konto)


    def testAddAccount(self):
        self.assertEqual(AccountRegistry.getAccountAmount(), 1)

    def testAddMultipleAccounts(self):
        AccountRegistry.addAccount(self.konto66)
        AccountRegistry.addAccount(self.konto77)
        self.assertEqual(AccountRegistry.getAccountAmount(), 3)
    
    @parameterized.expand([
        ("676756678", "676756678"),
        ("66666666666", "66666666666"),
        ("77777777777", "77777777777"),
        ("88888888", None)
    ])

    def testSearchByPesel(self, pesel, testResult):
        AccountRegistry.addAccount(self.konto66)
        AccountRegistry.addAccount(self.konto77)
        result = AccountRegistry.searchByPesel(pesel)
        self.assertEqual(result and result.pesel, testResult)
              
