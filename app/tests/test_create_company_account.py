import unittest

from ..CompanyAccount import CompanyAccount

class TestCreateCompanyAccount(unittest.TestCase):
    
    def setUp(self):
        self.companyName = "LovelyCompanyX"
        
    def testCreatingAccount(self):
        nip = "0123456789"
        new_company_acc = CompanyAccount(self.companyName, nip)
        self.assertEqual(new_company_acc.companyName, "LovelyCompanyX")
        self.assertEqual(new_company_acc.nip, "0123456789")
        self.assertEqual(new_company_acc.saldo, 0)
    
    def testWrongNip(self):
        nip = "12"
        new_company_acc = CompanyAccount(self.companyName, nip)
        self.assertEqual(new_company_acc.nip, "Niepoprawny NIP!")
