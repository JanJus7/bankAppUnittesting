class Konto:
    def __init__(self):
        self.saldo = 0
        self.historia = []

    def incomingTransfer(self, amount):
        self.saldo += amount
        self.historia.append(amount)

    def outgoingTransfer(self, amount):
        self.saldo -= amount
        self.historia.append(-amount)

    def outgoingExpressTransfer(self, amount):
        price = amount + self.expressFee
        self.saldo -= price
        self.historia.append(-amount)
        self.historia.append(-self.expressFee)
