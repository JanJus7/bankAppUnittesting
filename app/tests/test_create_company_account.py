import unittest
from parameterized import parameterized
from ..CompanyAccount import CompanyAccount
from unittest.mock import patch, MagicMock
import requests

class TestCreateCompanyAccount(unittest.TestCase):
    companyName = "Dariusz sp. z o.o."
        
    def testCreatingAccount(self):
        nip = "8461627563"
        firstCompanyAccount = CompanyAccount(self.companyName, nip)
        self.assertEqual(firstCompanyAccount.companyName, "Dariusz sp. z o.o.")
        self.assertEqual(firstCompanyAccount.nip, "8461627563")
        self.assertEqual(firstCompanyAccount.balance, 0)
    
    @parameterized.expand([
        ("0123456789", "0123456789"),
        ("aaaaaaaaab", "Niepoprawny NIP!"),
        ("123456789o", "Niepoprawny NIP!"),
        ("aaa1234567890aaa", "Niepoprawny NIP!"),
        ("1234567891234", "Niepoprawny NIP!"),
        ("12", "Niepoprawny NIP!"),
        ("123456789.", "Niepoprawny NIP!")
    ])
    def testNip(self, nip, result):
        new_company_acc = CompanyAccount(self.companyName, nip)
        self.assertEqual(new_company_acc.nip, result)

    @patch("requests.get")
    def testNipValidityCheckValidNip(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"message": "Valid NIP"}
        mock_get.return_value = mock_response

        result = CompanyAccount.nipValidityCheck("8461627563")
        self.assertTrue(result)
        mock_get.assert_called_once()

    @patch("requests.get")
    def testNipValidityCheckInvalidNip(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_response.json.return_value = {"message": "Invalid NIP"}
        mock_get.return_value = mock_response

        result = CompanyAccount.nipValidityCheck("8461627563")
        self.assertFalse(result)
        mock_get.assert_called_once()

    @patch("requests.get")
    def testNipValidityCheckRequestException(self, mock_get):
        mock_get.side_effect = requests.RequestException("API error")

        result = CompanyAccount.nipValidityCheck("8461627563")
        self.assertFalse(result)
        mock_get.assert_called_once()

    @patch("requests.get")
    def testConstructorRaisesValueErrorForUnregisteredCompany(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        with self.assertRaises(ValueError) as context:
            CompanyAccount(self.companyName, "8461627563")

        self.assertEqual(str(context.exception), "Company not registered!!")
        mock_get.assert_called_once()
