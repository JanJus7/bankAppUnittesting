import unittest
import requests

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