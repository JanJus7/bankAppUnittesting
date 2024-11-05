class Account:
    def __init__(self):
        self.balance = 0
        self.history = []

    def incomingTransfer(self, amount):
        self.balance += amount
        self.history.append(amount)

    def outgoingTransfer(self, amount):
        self.balance -= amount
        self.history.append(-amount)

    def outgoingExpressTransfer(self, amount):
        price = amount + self.expressFee
        self.balance -= price
        self.history.append(-amount)
        self.history.append(-self.expressFee)
