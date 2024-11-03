from .Konto import Konto

class CompanyAccount(Konto):

    expressFee = 5

    def __init__(self, companyName, nip):
        super().__init__()
        self.companyName = companyName
        if len(nip) == 10:
            self.nip = nip
        else:
            self.nip = "Niepoprawny NIP!"