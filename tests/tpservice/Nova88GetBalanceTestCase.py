import unittest
import requests
import json

class Nova88GetBalanceTestCase(unittest.TestCase):

    def setUp(self):
        self.url =  'http://10.4.194.28:55996/'

    def test_1_PT_GetBalance(self):
        data = { "TpId":27, "CustId":250032, "Inputs":{} }
        r = requests.post(self.url + 'API/GetBalance', json = data)
        result = json.loads(r.text)
        self.assertEquals(0, result["errorCode"])
        self.assertGreaterEqual(0, result["data"]["balance"])

    def test_2_Mega_GetBalance(self):
        data = { "TpId":22, "CustId":250032, "Inputs":{} }
        r = requests.post(self.url + 'API/GetBalance', json = data)
        result = json.loads(r.text)
        self.assertEquals(0, result["errorCode"])
        self.assertGreaterEqual(0, result["data"]["balance"])
