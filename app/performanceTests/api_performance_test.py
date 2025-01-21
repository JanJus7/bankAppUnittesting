import unittest
import requests
import time
import random

# API address
API_URL = "http://127.0.0.1:5000"

class TestApiPerformance(unittest.TestCase):

    def test_create_and_delete_accounts(self):
        for i in range(100):
            start_time = time.time()
            pesel = str(random.randint(10000000000, 99999999999))
            response = requests.post(
                f"{API_URL}/api/accounts",
                json={"name": "Jan", "surname": "Kowalski", "pesel": pesel},
                timeout=0.5
            )
            end_time = time.time()
            self.assertLess(
                end_time - start_time,
                0.5,
                f"Creating account {i+1} exceeded the time limit."
            )
            self.assertEqual(
                response.status_code,
                201,
                f"Account creation error {i+1}: {response.status_code}"
            )

            start_time = time.time()
            response = requests.delete(f"{API_URL}/api/accounts/{pesel}", timeout=0.5)
            end_time = time.time()
            self.assertLess(
                end_time - start_time,
                0.5,
                f"Deleting account {i+1} exceeded the time limit."
            )
            self.assertEqual(
                response.status_code,
                200,
                f"Account deletion error {i+1}: {response.status_code}"
            )
