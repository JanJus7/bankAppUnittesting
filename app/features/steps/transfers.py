from behave import *
import requests
from unittest_assertions import AssertEqual, AssertIn

assert_in = AssertIn()
assert_equal = AssertEqual()
URL = "http://localhost:5000"

@given('a personal account with a balance of {balance:d}')
def start_balance(context, balance):
    json_body = {
        "type": "incoming",
        "amount": balance
    }
    response = requests.post(URL + f"/api/accounts/{context.pesel}/transfer", json=json_body)
    assert_equal(response.status_code, 200)

@when('an outgoing transfer of {amount:d} is made')
def make_outgoing_transfer(context, amount):
    json_body = {
        "type": "outgoing",
        "amount": amount
    }
    response = requests.post(URL + f"/api/accounts/{context.pesel}/transfer", json=json_body)
    assert_equal(response.status_code, 200)

@when('an incoming transfer of {amount:d} is made')
def make_incoming_transfer(context, amount):
    json_body = {
        "type": "incoming",
        "amount": amount
    }
    response = requests.post(URL + f"/api/accounts/{context.pesel}/transfer", json=json_body)
    assert_equal(response.status_code, 200)

@when('an express transfer of {amount:d} is made')
def make_express_transfer(context, amount):
    json_body = {
        "type": "express",
        "amount": amount
    }
    response = requests.post(URL + f"/api/accounts/{context.pesel}/transfer", json=json_body)
    assert_equal(response.status_code, 200)

@then('the account balance is {expected_balance:d}')
def check_balance(context, expected_balance):
    response = requests.get(URL + f"/api/accounts/{context.pesel}")
    assert_equal(response.status_code, 200)
    data = response.json()
    assert_equal(data["balance"], expected_balance)

@then('the account history contains an outgoing transfer of {amount:d}')
def check_outgoing_transfer_in_history(context, amount):
    response = requests.get(URL + f"/api/accounts/{context.pesel}")
    assert_equal(response.status_code, 200)
    data = response.json()
    history = data["history"]
    assert_in(-amount, history)

@then('the account history contains an incoming transfer of {amount:d}')
def check_incoming_transfer_in_history(context, amount):
    response = requests.get(URL + f"/api/accounts/{context.pesel}")
    assert_equal(response.status_code, 200)
    data = response.json()
    history = data["history"]
    assert_in(amount, history)

@then('the account history contains an express transfer fee')
def check_express_transfer_fee_in_history(context):
    response = requests.get(URL + f"/api/accounts/{context.pesel}")
    assert_equal(response.status_code, 200)
    data = response.json()
    history = data["history"]
    assert_in(-1, history)
