class Konto:
    def __init__(self):
        self.saldo = 0

    def incomingTransfer(self, amount):
        self.saldo += amount

    def outgoingTransfer(self, amount):
        self.saldo -= amount

    def outgoingExpressTransfer(self, amount):
        price = amount + self.expressFee
        self.saldo -= price