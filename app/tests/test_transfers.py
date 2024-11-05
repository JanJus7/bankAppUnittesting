import unittest

from ..PersonalAccount import PersonalAccount
from ..CompanyAccount import CompanyAccount

class TestTransfers(unittest.TestCase):
    name = "Dariusz"
    surname = "Januszewski"
    pesel = "04251010644"

    companyName = "LovelyCompanyX"
    nip = "0123456789"

    def setUp(self):
        self.firstPersonalAccount = PersonalAccount(self.name, self.surname, self.pesel)
        self.firstCompanyAccount = CompanyAccount(self.companyName, self.nip)

    def testIncomesPersonalAcc(self):
        self.firstPersonalAccount.incomingTransfer(100)
        self.assertEqual(self.firstPersonalAccount.balance, 100, "Nie otrzymałeś jeszcze żadnego przelewu")

    def testOutgoingsPersonalAcc(self):
        self.firstPersonalAccount.incomingTransfer(100)
        self.firstPersonalAccount.outgoingTransfer(50)
        self.assertEqual(self.firstPersonalAccount.balance, 50, "Nie wykonałeś jeszcze przelewu!")
        self.assertGreaterEqual(self.firstPersonalAccount.balance, 0, "Ujemny Balans konta!")

    def testIncomesCompanyAcc(self):
        self.firstCompanyAccount.incomingTransfer(1500)
        self.assertEqual(self.firstCompanyAccount.balance, 1500, "Nie otrzymałeś jeszcze żadnego przelewu!")

    def testOutgoingsCompanyAcc(self):
        self.firstCompanyAccount.incomingTransfer(1000)
        self.firstCompanyAccount.outgoingTransfer(500)
        self.assertEqual(self.firstCompanyAccount.balance, 500, "Nie otrzymałeś jeszcze przelewu!")
        self.assertGreaterEqual(self.firstCompanyAccount.balance, 0, "Ujemny Bilans Konta!")

    def testExpressOutgoingsPersonalAcc(self):
        self.firstPersonalAccount.incomingTransfer(100)
        self.firstPersonalAccount.outgoingExpressTransfer(50)
        self.assertEqual(self.firstPersonalAccount.balance, 49, "Nie wykonałeś jeszcze przelewu!")
        self.assertGreaterEqual(self.firstPersonalAccount.balance, -1, "Ujemny Balans konta!")

    def testExpressOutgoingsCompanyAcc(self):
        self.firstCompanyAccount.incomingTransfer(1000)
        self.firstCompanyAccount.outgoingExpressTransfer(500)
        self.assertEqual(self.firstCompanyAccount.balance, 495, "Nie otrzymałeś jeszcze przelewu!")
        self.assertGreaterEqual(self.firstCompanyAccount.balance, -5, "Ujemny Bilans Konta!")

    def testHistoryLogPersonal(self):
        self.firstPersonalAccount.incomingTransfer(100)
        self.firstPersonalAccount.incomingTransfer(20)
        self.firstPersonalAccount.outgoingTransfer(20)
        self.firstPersonalAccount.incomingTransfer(21)
        self.firstPersonalAccount.outgoingExpressTransfer(20)
        self.assertEqual(self.firstPersonalAccount.history, [100, 20, -20, 21, -20, -1])

    def testHistoryCompany(self):
        self.firstCompanyAccount.incomingTransfer(100)
        self.firstCompanyAccount.incomingTransfer(20)
        self.firstCompanyAccount.outgoingTransfer(20)
        self.firstCompanyAccount.incomingTransfer(25)
        self.firstCompanyAccount.outgoingExpressTransfer(20)
        self.assertEqual(self.firstCompanyAccount.history, [100, 20, -20, 25, -20, -5])
