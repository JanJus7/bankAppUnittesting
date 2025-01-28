import json
from app.PersonalAccount import PersonalAccount

class AccountRegistry:
    registry = []

    @classmethod
    def addAccount(cls, account):
        if account not in cls.registry:
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

    @classmethod
    def dump_to_json(cls, filename="backup.json"):
        with open(filename, "w") as f:
            accounts_data = [
                {
                    "name": account.name,
                    "surname": account.surname,
                    "pesel": account.pesel,
                    "balance": account.balance,
                    "history": account.history
                }
                for account in cls.registry
            ]
            json.dump(accounts_data, f)
        return True

    @classmethod
    def load_from_json(cls, filename="backup.json"):
        with open(filename, "r") as f:
            accounts_data = json.load(f)
            cls.registry = []
            for account_data in accounts_data:
                account = PersonalAccount(
                    account_data["name"],
                    account_data["surname"],
                    account_data["pesel"]
                )
                account.balance = account_data["balance"]
                account.history = account_data["history"]
                cls.registry.append(account)
        return True