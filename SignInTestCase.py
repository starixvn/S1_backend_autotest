import unittest
import requests
import json

class SignInTestCase(unittest.TestCase):
    cookie = ''

    def setUp(self):
        self.url =  'https://www.n88dev.com/'
        self.account = 'autotest001'

    def test_1_login_with_wrong_password(self):

        data = {'UserName': self.account, 'Userpwd':'abcde',
                'isPersistent': True,'platform':'Win32','screen':'2560:1440:24','url':'https://www.n88dev.com',
                'userAgent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'}
        r = requests.post(self.url + 'api/Site/SignIn', json = data)
        result = json.loads(r.text)
        self.assertEquals(1001, result["errorCode"])

    def test_2_login_with_password(self):

        data = {'UserName': self.account, 'Userpwd':'autotest001!1',
                'isPersistent': True,'platform':'Win32','screen':'2560:1440:24','url':'https://www.n88dev.com',
                'userAgent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'}
        r = requests.post(self.url + 'api/Site/SignIn', json = data)
        result = json.loads(r.text)
        self.assertEquals(0, result["errorCode"])
        self.__class__.cookie = r.headers['Set-Cookie']

    def test_3_check_online(self):

        headers = {'Cookie': self.__class__.cookie}
        r = requests.post(self.url + 'api/Account/onlineCheck', headers = headers)
        result = json.loads(r.text)
        self.assertEquals(0, result["errorCode"])