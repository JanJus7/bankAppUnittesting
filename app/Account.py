class Account:
    def __init__(self):
        self.balance = 0
        self.history = []

    def incomingTransfer(self, amount):
        if amount > 0:
            self.balance += amount
            self.history.append(amount)

    def outgoingTransfer(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.history.append(-amount)
            return True
        return False
        

    def outgoingExpressTransfer(self, amount):
        if self.balance >= amount:    
            price = amount + self.expressFee
            self.balance -= price
            self.history.append(-amount)
            self.history.append(-self.expressFee)
            return True
        return False
