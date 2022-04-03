import unittest
import requests
import json
import os

class Nova88MYRTransferTestCase(unittest.TestCase):

    def setUp(self):
        self.custId = 643995

        env = os.getenv('Environment')
        if env == "Development":
            self.url = 'http://172.31.17.90:55996/'
        else:
            self.url = 'http://52.221.19.140:55996/'

    def test_01_Saba_TransferIn(self):

        data = {
            "TpId": 1,
            "CustId": self.custId,
            "Description": None,
            "Amount": 100.0,
            "direction": 1,
            "inputs": {
                "Host": "http://www.n88dev.com",
                "ClientIP": "218.32.244.12"
            }
        }
        r = requests.post(self.url + 'API/Transfer', json = data)
        result = json.loads(r.text)
        self.assertEquals(0, result["errorCode"])
        self.assertEquals(0, result["data"]["status"])

    def test_02_Saba_TransferOut(self):

        data = {
            "TpId": 1,
            "CustId": self.custId,
            "Description": None,
            "Amount": 100.0,
            "direction": 2,
            "inputs": {
                "Host": "http://www.n88dev.com",
                "ClientIP": "218.32.244.12"
            }
        }
        r = requests.post(self.url + 'API/Transfer', json = data)
        result = json.loads(r.text)
        self.assertEquals(0, result["errorCode"])
        self.assertEquals(0, result["data"]["status"])