class AccountRegistry:
    registry = []

    @classmethod
    def addAccount(cls, account):
        cls.registry.append(account)

    @classmethod
    def getAccountAmount(cls):
        return len(cls.registry)
    
    @classmethod
    def searchByPesel(cls, pesel):
        for account in cls.registry:
            if account.pesel == pesel:
                return account
        return None
    
    @classmethod
    def removeAccount(cls, account):
        if account in cls.registry:
            cls.registry.remove(account)
