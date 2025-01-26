from behave import *
import requests
from unittest_assertions import AssertEqual

assert_equal = AssertEqual()
URL = "http://localhost:5000"

def before_scenario(context, scenario):
    if "transfers" in scenario.tags:
        pesel = "12345678901"
        data = {
            "name": "Jan",
            "surname": "Kowalski",
            "pesel": pesel
        }
        response = requests.post(URL + "/api/accounts", json=data)
        assert_equal(response.status_code, 201)
        context.pesel = pesel

def after_scenario(context, scenario):
    if "transfers" in scenario.tags:
        response = requests.delete(f"{URL}/api/accounts/{context.pesel}")
        assert_equal(response.status_code, 200)
