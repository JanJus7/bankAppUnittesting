import unittest
import requests
import json
import os

class TestApiCRUD(unittest.TestCase):

    payload = {
        "name": "Dariusz",
        "surname": "Januszewski",
        "pesel": "67675667800"
    }

    url = 'http://127.0.0.1:5000/api/accounts'

    def tearDown(self):
        requests.delete(self.url + '/' + self.payload['pesel'])

    def testCreateAccount(self):
        r = requests.post(self.url, json=self.payload)
        self.assertEqual(r.status_code, 201)

    def testCreateExistingAccount(self):
        r = requests.post(self.url, json=self.payload)
        r = requests.post(self.url, json=self.payload)
        self.assertEqual(r.status_code, 409)

    def testAccountCount(self):
        requests.post(self.url, json=self.payload)
        r = requests.get(self.url + '/count')
        self.assertEqual(r.status_code, 202)
    
    def testGetAccountByPesel(self):
        requests.post(self.url, json=self.payload)
        r = requests.get(self.url + '/' + self.payload['pesel'])
        self.assertEqual(r.status_code, 200)

    def testGetNonExistentAccountByPesel(self):
        r = requests.get(self.url + '/12345678900')
        self.assertEqual(r.status_code, 404)

    def testUpdateAccount(self):
        requests.post(self.url, json=self.payload)
        r = requests.patch(self.url + '/' + self.payload['pesel'], json={"name": "Janusz"})
        self.assertEqual(r.status_code, 200)

    def testUpdateNonExistingAccount(self):
        r = requests.patch(self.url + '/12345678900', json={"name": "Janusz"})
        self.assertEqual(r.status_code, 404)

    def testDeleteAccount(self):
        requests.post(self.url, json=self.payload)
        r = requests.delete(self.url + '/' + self.payload['pesel'])
        self.assertEqual(r.status_code, 200)

    def testDeleteNonExistingAccount(self):
        r = requests.delete(self.url + '/12345678900')
        self.assertEqual(r.status_code, 404)

    def test_create_backup(self):
        r = requests.post(self.url + '/backup')
        self.assertEqual(r.status_code, 200)

    def test_restore_backup(self):
        with open("backup.json", "w") as f:
            json.dump([
                {"name": "Jan", "surname": "Kowalski", "pesel": "11111111111", "balance": 100, "history": []},
                {"name": "Anna", "surname": "Nowak", "pesel": "22222222222", "balance": 200, "history": []}
            ], f)

        r = requests.post(self.url + '/restore')
        self.assertEqual(r.status_code, 200)

        r = requests.get(self.url + '/count')
        self.assertEqual(r.status_code, 202)
        data = r.json()
        actual_count = data['message'].split(': ')[1]
        self.assertEqual(actual_count, "2")

    def tearDown(self):
        try:
            os.remove("backup.json")
        except FileNotFoundError:
            pass