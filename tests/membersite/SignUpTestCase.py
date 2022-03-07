import unittest
import requests
import json
import datetime,random

class SignUpTestCase(unittest.TestCase):

    def setUp(self):
        self.url =  'https://www.n88dev.com/'
        dt = datetime.datetime.today()
        self.user_name = 'test' + dt.strftime('%m%d%H%M%S')
        randomlist = random.sample(range(0, 999), 3)
        self.phone_number = f'{randomlist[0]}{randomlist[1]}{randomlist[2]}'
        self.mail = f'{self.user_name}@test.com'

    def test_1_ExistsUserName_And_Exists(self):

        data = {'UserName':'test123'}
        r = requests.post(self.url + 'api/Site/ExistsUserName/cs', json = data)
        result = json.loads(r.text)
        self.assertTrue(result["data"])

    def test_2_ExistsUserName_Not_Exists(self):

        data = {'UserName': self.user_name}
        r = requests.post(self.url + 'api/Site/ExistsUserName/cs', json = data)
        result = json.loads(r.text)
        self.assertFalse(result["data"])

    def test_3_ExistsEmail_And_Exists(self):

        data = {'Email':'abcdefg@hhh.com'}
        r = requests.post(self.url + 'api/Site/ExistsEmail', json = data)
        result = json.loads(r.text)
        self.assertTrue(result["data"])

    def test_4_ExistsEmail_Not_Exists(self):

        data = {'Email': f'{self.mail}'}
        r = requests.post(self.url + 'api/Site/ExistsEmail', json = data)
        result = json.loads(r.text)
        self.assertFalse(result["data"])

    def test_5_ExistsPhoneNo_And_Exists(self):

        data = {'AreaCode': '+66', 'PhoneNo': '777878787'}
        r = requests.post(self.url + 'api/Site/ExistsPhoneNo', json = data)
        result = json.loads(r.text)
        self.assertTrue(result["data"])

    def test_6_ExistsPhoneNo_Not_Exists(self):

        data = {'AreaCode': '+66', 'PhoneNo': self.phone_number}
        r = requests.post(self.url + 'api/Site/ExistsPhoneNo', json = data)
        result = json.loads(r.text)
        self.assertFalse(result["data"])

    def test_7_SignUp_without_affCode(self):

        data = {'AreaCode': '+66', 'CurrencyId': 4, 'UserLang':'cs', 'UserName': self.user_name, 'Userpwd': f'test!1', 'Email': f'{self.mail}', 'PhoneNo': self.phone_number}
        r = requests.post(self.url + 'api/Site/Signup/cs', json = data)
        result = json.loads(r.text)
        self.assertEquals(0, result["errorCode"])