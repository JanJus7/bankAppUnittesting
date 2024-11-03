import unittest

from ..PersonalAccount import PersonalAccount
from ..CompanyAccount import CompanyAccount

class TestTransfers(unittest.TestCase):
    def setUp(self):
        self.imie = "Dariusz"
        self.nazwisko = "Januszewski"
        self.numerPESEL = "04251010644"

        self.companyName = "FirmaTest"
        self.nip = "0123456789"

    def testIncomesPersonalAcc(self):
        pierwsze_konto = PersonalAccount(self.imie, self.nazwisko, self.numerPESEL)
        pierwsze_konto.incomingTransfer(100)
        self.assertEqual(pierwsze_konto.saldo, 100, "Nie otrzymałeś jeszcze żadnego przelewu")

    def testOutgoingsPersonalAcc(self):
        pierwsze_konto = PersonalAccount(self.imie, self.nazwisko, self.numerPESEL)
        pierwsze_konto.incomingTransfer(100)
        pierwsze_konto.outgoingTransfer(50)
        self.assertEqual(pierwsze_konto.saldo, 50, "Nie wykonałeś jeszcze przelewu!")
        self.assertGreaterEqual(pierwsze_konto.saldo, 0, "Ujemny Balans konta!")

    def testIncomesCompanyAcc(self):
        new_company_acc = CompanyAccount(self.companyName, self.nip)
        new_company_acc.incomingTransfer(1500)
        self.assertEqual(new_company_acc.saldo, 1500, "Nie otrzymałeś jeszcze żadnego przelewu!")

    def testOutgoingsCompanyAcc(self):
        new_company_acc = CompanyAccount(self.companyName, self.nip)
        new_company_acc.incomingTransfer(1000)
        new_company_acc.outgoingTransfer(500)
        self.assertEqual(new_company_acc.saldo, 500, "Nie otrzymałeś jeszcze przelewu!")
        self.assertGreaterEqual(new_company_acc.saldo, 0, "Ujemny Bilans Konta!")

    def testExpressOutgoingsPersonalAcc(self):
        pierwsze_konto = PersonalAccount(self.imie, self.nazwisko, self.numerPESEL)
        pierwsze_konto.incomingTransfer(100)
        pierwsze_konto.outgoingExpressTransfer(50)
        self.assertEqual(pierwsze_konto.saldo, 49, "Nie wykonałeś jeszcze przelewu!")
        self.assertGreaterEqual(pierwsze_konto.saldo, -1, "Ujemny Balans konta!")

    def testExpressOutgoingsCompanyAcc(self):
        new_company_acc = CompanyAccount(self.companyName, self.nip)
        new_company_acc.incomingTransfer(1000)
        new_company_acc.outgoingExpressTransfer(500)
        self.assertEqual(new_company_acc.saldo, 495, "Nie otrzymałeś jeszcze przelewu!")
        self.assertGreaterEqual(new_company_acc.saldo, -5, "Ujemny Bilans Konta!")