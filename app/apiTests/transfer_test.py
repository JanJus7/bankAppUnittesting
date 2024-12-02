import unittest
import requests

class TestTransferCRUD(unittest.TestCase):

    payload = {
        "name": "Dariusz",
        "surname": "Januszewski",
        "pesel": "67675667800"
    }

    payload2 = {
        "amount": 500,
        "type": "incoming"
    }

    payload3 = {
        "amount": 500,
        "type": "outgoing"
    }

    payload3f = {
        "amount": 501,
        "type": "outgoing"
    }

    payload4 = {
        "amount": 500,
        "type": "express"
    }

    payload4f = {
        "amount": 501,
        "type": "express"
    }

    payload5 = {
        "amount": 666,
        "type": "press"
    }




    pesel = payload["pesel"]

    url = 'http://127.0.0.1:5000/api/accounts'

    def setUp(self):
        r = requests.post(self.url, json=self.payload)
        self.assertEqual(r.status_code, 201)
        r = requests.post(self.url + "/" + self.payload["pesel"] + "/transfer", json=self.payload2)
        self.assertEqual(r.status_code, 200)

    def tearDown(self):
        r = requests.delete(self.url + '/' + self.payload['pesel'])
        self.assertEqual(r.status_code, 200)

    def testAccountNotFound(self):
        r = requests.post(self.url + "/11/transfer", json=self.payload2)
        self.assertEqual(r.status_code, 404)
    
    def testOutgoingTransfer(self):
        r = requests.post(self.url + "/" + self.payload["pesel"] + "/transfer", json=self.payload3)
        self.assertEqual(r.status_code, 200)

    def testOutgoingTransferFail(self):
        r = requests.post(self.url + "/" + self.payload["pesel"] + "/transfer", json=self.payload3f)
        self.assertEqual(r.status_code, 422)
    
    def testExpressTransfer(self):
        r = requests.post(self.url + "/" + self.payload["pesel"] + "/transfer", json=self.payload4)
        self.assertEqual(r.status_code, 200)

    def testExpressTransferFail(self):
        r = requests.post(self.url + "/" + self.payload["pesel"] + "/transfer", json=self.payload4f)
        self.assertEqual(r.status_code, 422)

    def testWrongType(self):
        r =requests.post(self.url + "/" + self.payload["pesel"] + "/transfer", json=self.payload5)
        self.assertEqual(r.status_code, 422)

      
