from flask import Flask, request, jsonify
from app.AccountRegistry import AccountRegistry
from app.PersonalAccount import PersonalAccount

app = Flask(__name__)

@app.route("/api/accounts", methods=['POST'])
def create_account():
    data = request.get_json()
    print(f"Create account request: {data}")
    konto = PersonalAccount(data["name"], data["surname"], data["pesel"])
    if AccountRegistry.searchByPesel(konto.pesel):
        return jsonify({"message": "Account already exists"}), 409
    else:
        AccountRegistry.addAccount(konto)
        return jsonify({"message": "Account created"}), 201

@app.route("/api/accounts/count", methods=['GET'])
def account_count():
    result = AccountRegistry.getAccountAmount()
    return jsonify({"message": f"Number of accounts: {result}"}), 202


@app.route("/api/accounts/<pesel>", methods=['GET'])
def get_account_by_pesel(pesel):
    account = AccountRegistry.searchByPesel(pesel)
    if account:
        return jsonify({"name": account.name, "surname": account.surname, "pesel": account.pesel }), 200
    else:
        return jsonify({"message": "Account not found"}), 404

@app.route("/api/accounts/<pesel>", methods=['PATCH'])
def update_account(pesel):
    data = request.get_json()
    account = AccountRegistry.searchByPesel(pesel)
    if not account:
        return jsonify({"message": "Account not found"}), 404

    if "name" in data:
        account.name = data["name"]
    if "surname" in data:
        account.surname = data["surname"]
    
    return jsonify({"message": "Account updated"}), 200

@app.route("/api/accounts/<pesel>", methods=['DELETE'])
def delete_account(pesel):
    account = AccountRegistry.searchByPesel(pesel)
    if not account:
        return jsonify({"message": "Account not found"}), 404

    AccountRegistry.removeAccount(account)
    return jsonify({"message": "Account deleted"}), 200

@app.route("/api/accounts/<pesel>/transfer", methods=['POST'])
def transfers(pesel):
    data = request.get_json()
    account = AccountRegistry.searchByPesel(pesel)
    
    if not account:
        return jsonify({"message": "Account not found"}), 404
    else:
        if data["type"] == "incoming":
            account.incomingTransfer(data["amount"])
            return jsonify({"message": "Order accepted for execution"}), 200
        elif data["type"] == "outgoing":
            if account.outgoingTransfer(data["amount"]):
                return jsonify({"message": "Order accepted for execution"}), 200
            else:
                return jsonify({"message": "Insufficient funds"}), 422
        elif data["type"] == "express":
            if account.outgoingExpressTransfer(data["amount"]):
                return jsonify({"message": "Order accepted for execution"}), 200
            else:
                return jsonify({"message": "Insufficient funds"}), 422
        else:
            return jsonify({"message": "Unprocessable entity"}), 422

