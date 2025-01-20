import unittest
from unittest.mock import MagicMock, patch
from ..PersonalAccount import PersonalAccount
from ..CompanyAccount import CompanyAccount
from datetime import date

class TestSendHistoryToEmail(unittest.TestCase):

    @patch("app.PersonalAccount.date")
    def test_send_history_to_email_personal_account_success(self, mock_date):
        mock_date.today.return_value = date(2024, 12, 10)
        smtp_client = MagicMock()
        account = PersonalAccount("Jan", "Kowalski", "12345678901")
        account.history = [100, -1, 500]

        smtp_client.send.return_value = True

        result = account.send_history_to_email(smtp_client, "jan.kowalski@example.com")

        self.assertTrue(result)
        smtp_client.send.assert_called_once_with(
            "Statement from 2024-12-10",
            "Your account history is: [100, -1, 500]",
            "jan.kowalski@example.com"
        )

    @patch("app.PersonalAccount.date")
    def test_send_history_to_email_personal_account_failure(self, mock_date):
        mock_date.today.return_value = date(2024, 12, 10)
        smtp_client = MagicMock()
        account = PersonalAccount("Jan", "Kowalski", "12345678901")
        account.history = [100, -1, 500]

        smtp_client.send.return_value = False

        result = account.send_history_to_email(smtp_client, "jan.kowalski@example.com")

        self.assertFalse(result)
        smtp_client.send.assert_called_once_with(
            "Statement from 2024-12-10",
            "Your account history is: [100, -1, 500]",
            "jan.kowalski@example.com"
        )

    @patch("app.CompanyAccount.date")
    @patch("app.CompanyAccount.CompanyAccount.nipValidityCheck")
    def test_send_history_to_email_company_account_success(self, mock_nip_check, mock_date):
        mock_date.today.return_value = date(2024, 12, 10)
        mock_nip_check.return_value = True
        smtp_client = MagicMock()
        account = CompanyAccount("Firma XYZ", "1234567890")
        account.history = [5000, -1000, 500]

        smtp_client.send.return_value = True

        result = account.send_history_to_email(smtp_client, "firma.xyz@example.com")

        self.assertTrue(result)
        smtp_client.send.assert_called_once_with(
            "Statement from 2024-12-10",
            "Your company account history is: [5000, -1000, 500]",
            "firma.xyz@example.com"
        )

    @patch("app.CompanyAccount.date")
    @patch("app.CompanyAccount.CompanyAccount.nipValidityCheck")
    def test_send_history_to_email_company_account_failure(self, mock_nip_check, mock_date):
        mock_date.today.return_value = date(2024, 12, 10)
        mock_nip_check.return_value = True
        smtp_client = MagicMock()
        account = CompanyAccount("Firma XYZ", "1234567890")
        account.history = [5000, -1000, 500]

        smtp_client.send.return_value = False

        result = account.send_history_to_email(smtp_client, "firma.xyz@example.com")

        self.assertFalse(result)
        smtp_client.send.assert_called_once_with(
            "Statement from 2024-12-10",
            "Your company account history is: [5000, -1000, 500]",
            "firma.xyz@example.com"
        )