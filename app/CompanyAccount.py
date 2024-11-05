import re
from .Account import Account

class CompanyAccount(Account):

    expressFee = 5

    def __init__(self, companyName, nip):
        super().__init__()
        self.companyName = companyName
        if re.match("^[0-9]{10}$", nip):
            self.nip = nip
        else:
            self.nip = "Niepoprawny NIP!"