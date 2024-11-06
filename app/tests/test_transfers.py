import unittest
from parameterized import parameterized
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

    @parameterized.expand([
        (100, 50, 50),
        (50, 50, 0),
        (49, 50, 49)
    ])

    def testOutgoingsPersonalAcc(self, accBalance, lost, result):
        self.firstPersonalAccount.balance = accBalance
        self.firstPersonalAccount.outgoingTransfer(lost)
        self.assertEqual(self.firstPersonalAccount.balance, result, "Nie wykonałeś jeszcze przelewu!")

    def testIncomesCompanyAcc(self):
        self.firstCompanyAccount.incomingTransfer(1500)
        self.assertEqual(self.firstCompanyAccount.balance, 1500, "Nie otrzymałeś jeszcze żadnego przelewu!")

    @parameterized.expand([
        (100, 50, 50),
        (50, 50, 0),
        (49, 50, 49)
    ])
        
    def testOutgoingsCompanyAcc(self, accBalance, lost, result):
        self.firstCompanyAccount.incomingTransfer(accBalance)
        self.firstCompanyAccount.outgoingTransfer(lost)
        self.assertEqual(self.firstCompanyAccount.balance, result, "Nie otrzymałeś jeszcze przelewu!")

    @parameterized.expand([
        (100, 50, 49),
        (50, 50, -1),
        (49, 50, 49)
    ])
        
    def testExpressOutgoingsPersonalAcc(self, accBalance, lost, result):
        self.firstPersonalAccount.incomingTransfer(accBalance)
        self.firstPersonalAccount.outgoingExpressTransfer(lost)
        self.assertEqual(self.firstPersonalAccount.balance, result, "Nie wykonałeś jeszcze przelewu!")

    @parameterized.expand([
        (100, 50, 45),
        (50, 50, -5),
        (49, 50, 49)
    ])

    def testExpressOutgoingsCompanyAcc(self, accBalance, lost, result):
        self.firstCompanyAccount.incomingTransfer(accBalance)
        self.firstCompanyAccount.outgoingExpressTransfer(lost)
        self.assertEqual(self.firstCompanyAccount.balance, result, "Nie otrzymałeś jeszcze przelewu!")

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
