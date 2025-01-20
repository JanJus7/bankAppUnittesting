import re
from .Account import Account
import requests
import os
import datetime
from datetime import date

class CompanyAccount(Account):

    expressFee = 5

    def __init__(self, companyName, nip):
        super().__init__()
        self.companyName = companyName
        if re.match("^[0-9]{10}$", nip):
            self.nip = nip
            if not self.nipValidityCheck(nip):
                raise ValueError("Company not registered!!")
        else:
            self.nip = "Niepoprawny NIP!"

    def takeLoan(self, amount):
        flag = False
        for i in self.history:
            if i == -1775:
                flag = True
                break
        if flag == True and self.balance >= (2*amount):
            self.balance += amount
            self.history.append(amount)

    @classmethod
    def nipValidityCheck(cls, nip):
        url = os.getenv('BANK_APP_MF_URL', 'https://wl-test.mf.gov.pl/')
        today = datetime.datetime.today().strftime('%Y-%m-%d')
        urlF = url + f"api/search/nip/{nip}?date={today}"
        print(f"Sending requests to {urlF}")
        try:
            response = requests.get(urlF)
            print(f"Response code is: {response.status_code}, {response.json()}")
            if response.status_code == 200:
                return True
        except requests.RequestException as e:
            print(f"An error occurred: {e}")
        return False
    
    def send_history_to_email(self, smtp_client, recipient):
        history_str = str(self.history)
        subject = f"Statement from {date.today().strftime('%Y-%m-%d')}"
        body = f"Your company account history is: {history_str}"
        return smtp_client.send(subject, body, recipient)