import unittest
import requests
import json
import os

class Nova88MYRGetBalanceTestCase(unittest.TestCase):

    def setUp(self):
        self.custId = 643995

        env = os.getenv('Environment')
        if env == "Development":
            self.url = 'http://172.31.17.90:55996/'
        else:
            self.url = 'http://52.221.19.140:55996/'

    def test_01_Saba_GetBalance(self):
        data = { "TpId":1, "CustId":self.custId, "Inputs":{} }
        r = requests.post(self.url + 'API/GetBalance', json = data)
        result = json.loads(r.text)
        self.assertEquals(0, result["errorCode"])
        self.assertGreaterEqual(0, result["data"]["balance"])

    def test_02_918Kiss_GetBalance(self):
        data = { "TpId":21, "CustId":self.custId, "Inputs":{} }
        r = requests.post(self.url + 'API/GetBalance', json = data)
        result = json.loads(r.text)
        self.assertEquals(0, result["errorCode"])
        self.assertGreaterEqual(0, result["data"]["balance"])

    def test_03_PT_GetBalance(self):
        data = { "TpId":22, "CustId":self.custId, "Inputs":{} }
        r = requests.post(self.url + 'API/GetBalance', json = data)
        result = json.loads(r.text)
        self.assertEquals(0, result["errorCode"])
        self.assertGreaterEqual(0, result["data"]["balance"])

    def test_04_Mega_GetBalance(self):
        data = { "TpId":27, "CustId":self.custId, "Inputs":{} }
        r = requests.post(self.url + 'API/GetBalance', json = data)
        result = json.loads(r.text)
        self.assertEquals(5003, result["errorCode"])
        self.assertGreaterEqual(0, result["data"]["balance"])
