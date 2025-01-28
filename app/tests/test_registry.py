import unittest
from parameterized import parameterized
from ..PersonalAccount import PersonalAccount
from ..AccountRegistry import AccountRegistry
import os
import json

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
        self.konto = PersonalAccount(self.imie, self.nazwisko, self.pesel)
        AccountRegistry.addAccount(self.konto)


    def testAddAccount(self):
        self.assertEqual(AccountRegistry.getAccountAmount(), 1)

    def testAddExistingAccount(self):
        AccountRegistry.addAccount(self.konto)
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

    def testRemoveAccount(self):
        AccountRegistry.removeAccount(self.konto)
        self.assertEqual(AccountRegistry.getAccountAmount(), 0)

    def testRemoveNonExistingAccount(self):
        non_existent_account = PersonalAccount("Fake", "User", "99999999999")
        AccountRegistry.removeAccount(non_existent_account)
        self.assertEqual(AccountRegistry.getAccountAmount(), 1)

    def test_dump_to_json(self):
        AccountRegistry.addAccount(self.konto66)
        AccountRegistry.addAccount(self.konto77)
        self.assertTrue(AccountRegistry.dump_to_json())
        self.assertTrue(os.path.exists("backup.json"))

        with open("backup.json", "r") as f:
            data = json.load(f)
        self.assertEqual(len(data), 3)
        self.assertEqual(data[0]["pesel"], self.pesel)
        self.assertEqual(data[1]["pesel"], self.pesel66)
        self.assertEqual(data[2]["pesel"], self.pesel77)

    def test_load_from_json(self):
        with open("backup.json", "w") as f:
            json.dump([
                {"name": "Jan", "surname": "Kowalski", "pesel": "11111111111", "balance": 100, "history": []},
                {"name": "Anna", "surname": "Nowak", "pesel": "22222222222", "balance": 200, "history": []}
            ], f)

        self.assertTrue(AccountRegistry.load_from_json())
        self.assertEqual(AccountRegistry.getAccountAmount(), 2)
        self.assertEqual(AccountRegistry.searchByPesel("11111111111").balance, 100)
        self.assertEqual(AccountRegistry.searchByPesel("22222222222").balance, 200)

    def tearDown(self):
        try:
            os.remove("backup.json")
        except FileNotFoundError:
            pass