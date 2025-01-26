import unittest
from parameterized import parameterized
from ..PersonalAccount import PersonalAccount
from ..CompanyAccount import CompanyAccount

class TestLoan(unittest.TestCase):
    name = "Dariusz"
    surname = "Januszewski"
    pesel = "04251010644"

    companyName = "LovelyCompanyX"
    nip = "0123456789"

    def setUp(self):
        self.firstPersonalAccount = PersonalAccount(self.name, self.surname, self.pesel)
        self.firstCompanyAccount = CompanyAccount(self.companyName, self.nip)

    @parameterized.expand([
        ([100, 500, 600], 500, 500, [100, 500, 600, 500]),
        ([1, -500, 10], 500, 0, [1, -500, 10]),
        ([100, 200, -99], 200, 0, [100, 200, -99]),
        ([100, 200], 200, 0, [100, 200]),
        ([10000, -1, 5000, 100000], 10, 0, [10000, -1, 5000, 100000]),
        ([600, 500, 200, -100, -200, -100], 200, 200, [600, 500, 200, -100, -200, -100, 200]),
        ([-100, -200, -400, -100, 200], 700, 0, [-100, -200, -400, -100, 200])
    ])


    def testLoanPersonalAcc(self, history, loanAmount, expectedBalance, expectedHistory):
        self.firstPersonalAccount.history = history
        self.firstPersonalAccount.takeLoan(loanAmount)
        self.assertEqual(self.firstPersonalAccount.balance, expectedBalance)
        self.assertEqual(self.firstPersonalAccount.history, expectedHistory, "historia nie została zaktualizowana")

    @parameterized.expand([
        (1001, [100, 500, 600, 2000, -1775], 500, 1501, [100, 500, 600, 2000, -1775, 500]),
        (1001, [100, 500, 600, -1775, 2000], 500, 1501, [100, 500, 600, -1775, 2000, 500]),
        (1001, [100, 500, -1775, 600, 2000], 500, 1501, [100, 500, -1775, 600, 2000, 500]),
        (1001, [100, -1775, 500, 600, 2000], 500, 1501, [100, -1775, 500, 600, 2000, 500]),
        (1001, [-1775, 100, 500, 600, 2000], 500, 1501, [-1775, 100, 500, 600, 2000, 500]),
        (1000, [100, 500, 600, 2000, -1775], 500, 1500, [100, 500, 600, 2000, -1775, 500]),
        (1001, [100, 500, 600, 2000, 1775], 500, 1001, [100, 500, 600, 2000, 1775]),
        (999, [100, 500, 600, 2000, -1775], 500, 999, [100, 500, 600, 2000, -1775]),
        (999, [100, 500, 600, 2000, 1775], 500, 999, [100, 500, 600, 2000, 1775]),
        (0, [], 500, 0, []),
        (1000, [], 500, 1000, [])
    ])


    def testLoanCompanyAcc(self, balance, history, loanAmount, expeactedBalance, expectedHistory):
        self.firstCompanyAccount.balance = balance
        self.firstCompanyAccount.history = history
        self.firstCompanyAccount.takeLoan(loanAmount)
        self.assertEqual(self.firstCompanyAccount.balance, expeactedBalance)
        self.assertEqual(self.firstCompanyAccount.history, expectedHistory, "historia nie została zaktualizowana")