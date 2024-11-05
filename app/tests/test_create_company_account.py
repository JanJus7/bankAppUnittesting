import unittest

from ..CompanyAccount import CompanyAccount

class TestCreateCompanyAccount(unittest.TestCase):
    companyName = "LovelyCompanyX"
        
    def testCreatingAccount(self):
        nip = "0123456789"
        firstCompanyAccount = CompanyAccount(self.companyName, nip)
        self.assertEqual(firstCompanyAccount.companyName, "LovelyCompanyX")
        self.assertEqual(firstCompanyAccount.nip, "0123456789")
        self.assertEqual(firstCompanyAccount.balance, 0)
    
    def testWrongNip(self):
        nip = "12"
        new_company_acc = CompanyAccount(self.companyName, nip)
        self.assertEqual(new_company_acc.nip, "Niepoprawny NIP!")
