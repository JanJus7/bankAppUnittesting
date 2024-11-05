import unittest
from ..CompanyAccount import CompanyAccount
from parameterized import parameterized

class TestCreateCompanyAccount(unittest.TestCase):
    companyName = "LovelyCompanyX"
        
    def testCreatingAccount(self):
        nip = "0123456789"
        firstCompanyAccount = CompanyAccount(self.companyName, nip)
        self.assertEqual(firstCompanyAccount.companyName, "LovelyCompanyX")
        self.assertEqual(firstCompanyAccount.nip, "0123456789")
        self.assertEqual(firstCompanyAccount.balance, 0)
    
    @parameterized.expand([
        ("0123456789", "0123456789"),
        ("aaaaaaaaaa", "Niepoprawny NIP!"),
        ("123456789o", "Niepoprawny NIP!"),
        ("aaa1234567890aaa", "Niepoprawny NIP!"),
        ("1234567891234", "Niepoprawny NIP!"),
        ("12", "Niepoprawny NIP!"),
        ("123456789.", "Niepoprawny NIP!")
    ])
    def testNip(self, nip, result):
        new_company_acc = CompanyAccount(self.companyName, nip)
        self.assertEqual(new_company_acc.nip, result)
