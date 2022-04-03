import unittest
import requests
import json
import pymysql.cursors
import os

class Nova88MYRLoginTestCase(unittest.TestCase):

    def setUp(self):
        self.url =  'https://www.n88dev.com/'
        self.custId = 643995

        env = os.getenv('Environment')
        if env == "Development":
            self.tpsUrl = 'http://172.31.17.90:55996/'
            self.mysql = '172.31.20.107'
        else:
            self.tpsUrl = 'http://52.221.19.140:55996/'
            self.mysql = '13.250.152.76'

    def test_00_init(self):

        data = {
            'UserName': 'autotestmyr',
            'Userpwd':'a123456!',
            'isPersistent': True,
            'platform':'Win32',
            'screen':'2560:1440:24',
            'url':'https://www.n88dev.com',
            'userAgent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
        }

        r = requests.post(self.url + 'api/Site/SignIn', json = data)
        result = json.loads(r.text)
        self.assertEquals(0, result['errorCode'])

        # Connect to the database
        connection = pymysql.connect(host = self.mysql,
                                     user = 'api_caching_sha2',
                                     password = 'Aa87654321!!!',
                                     database = 'Siebog',
                                     cursorclass = pymysql.cursors.DictCursor)

        with connection:
            with connection.cursor() as cursor:
                # Read a single record
                sql = 'SELECT t.Token FROM Siebog.OnUser t WHERE CustId=%s LIMIT 1;'
                cursor.execute(sql, (self.custId,))
                result = cursor.fetchone()
                self.__class__.token = result['Token']

    def test_01_Saba_Soccer_Login(self):

        token = self.__class__.token
        data = {
            'TpId': 1,
            'CustId': self.custId,
            'LangId': 'en',
            'AppType': 1,
            'SiteId': 1,
            'inputs': {
                'homeUrl': 'http://www.n88dev.com',
                'signupUrl': 'http://www.n88dev.com/join',
                'LoginUrl': 'http://www.n88dev.com/login',
                'tpId': '1',
                'gameId': '1',
                'CashierUrl': 'http://www.n88dev.com/deposit',
                'errorUrl': 'https://error.0814media.net/404/index_en.html',
                'tpGameType': '1',
                'Host': 'http://www.n88dev.com',
                'ClientIP': '218.32.244.12',
                'Token': token
            }
        }

        r = requests.post(self.tpsUrl + 'API/GotoGame', json = data)
        result = json.loads(r.text)
        self.assertEquals(result['errorCode'], 0)
        self.assertRegex(result['message'], 'https?:\/\/')

    def test_02_Saba_Tennis_Login(self):

        token = self.__class__.token
        data = {
            'TpId': 1,
            'CustId': self.custId,
            'LangId': 'en',
            'AppType': 1,
            'SiteId': 1,
            'inputs': {
                'homeUrl': 'http://www.n88dev.com',
                'signupUrl': 'http://www.n88dev.com/join',
                'LoginUrl': 'http://www.n88dev.com/login',
                'tpId': '1',
                'gameId': '5',
                'CashierUrl': 'http://www.n88dev.com/deposit',
                'errorUrl': 'https://error.0814media.net/404/index_th_en.html',
                'tpGameType': '1',
                'Host': 'http://www.n88dev.com',
                'ClientIP': '218.32.244.12',
                'Token': token
            }
        }

        r = requests.post(self.tpsUrl + 'API/GotoGame', json = data)
        result = json.loads(r.text)
        self.assertEquals(result['errorCode'], 0)
        self.assertRegex(result['message'], 'https?:\/\/')

    def test_03_Saba_VirtualSports_Login(self):

        token = self.__class__.token
        data = {
            'TpId': 1,
            'CustId': self.custId,
            'LangId': 'en',
            'AppType': 1,
            'SiteId': 1,
            'inputs': {
                'homeUrl': 'http://www.n88dev.com',
                'signupUrl': 'http://www.n88dev.com/join',
                'LoginUrl': 'http://www.n88dev.com/login',
                'tpId': '1',
                'gameId': '192',
                'CashierUrl': 'http://www.n88dev.com/deposit',
                'errorUrl': 'https://error.0814media.net/404/index_th_en.html',
                'tpGameType': '24',
                'Host': 'http://www.n88dev.com',
                'ClientIP': '218.32.244.12',
                'Token': token
            }
        }

        r = requests.post(self.tpsUrl + 'API/GotoGame', json = data)
        result = json.loads(r.text)
        self.assertEquals(result['errorCode'], 0)
        self.assertRegex(result['message'], 'https?:\/\/')

    def test_04_Saba_ESports_Login(self):

        token = self.__class__.token
        data = {
            'TpId': 1,
            'CustId': self.custId,
            'LangId': 'en',
            'AppType': 1,
            'SiteId': 1,
            'inputs': {
                'homeUrl': 'http://www.n88dev.com',
                'signupUrl': 'http://www.n88dev.com/join',
                'LoginUrl': 'http://www.n88dev.com/login',
                'tpId': '1',
                'gameId': '43',
                'CashierUrl': 'http://www.n88dev.com/deposit',
                'bettype': '1',
                'errorUrl': 'https://error.0814media.net/404/index_th_en.html',
                'tpGameType': '1',
                'Host': 'http://www.n88dev.com',
                'ClientIP': '218.32.244.12',
                'Token': token
            }
        }

        r = requests.post(self.tpsUrl + 'API/GotoGame', json = data)
        result = json.loads(r.text)
        self.assertEquals(result['errorCode'], 0)
        self.assertRegex(result['message'], 'https?:\/\/')

    def test_05_PP_LiveCasino_Login(self):

        token = self.__class__.token
        data = {
            "TpId": 5,
            "CustId": self.custId,
            "LangId": "en",
            "AppType": 1,
            "SiteId": 1,
            "inputs": {
                "homeUrl": "http://www.n88dev.com",
                "signupUrl": "http://www.n88dev.com/join",
                "LoginUrl": "http://www.n88dev.com/login",
                "tpId": "5",
                "gameId": "101",
                "CashierUrl": "http://www.n88dev.com/deposit",
                "errorUrl": "https://error.0814media.net/404/index_en.html",
                "tpGameType": "16",
                "Host": "http://www.n88dev.com",
                "ClientIP": "218.32.244.12",
                "Token": token
            }
        }

        r = requests.post(self.tpsUrl + 'API/GotoGame', json = data)
        result = json.loads(r.text)
        self.assertEquals(result['errorCode'], 0)
        self.assertRegex(result['message'], 'https?:\/\/')

    def test_06_EVO_LiveCasino_Login(self):

            token = self.__class__.token
            data = {
                "TpId": 36,
                "CustId": self.custId,
                "LangId": "en",
                "AppType": 1,
                "SiteId": 1,
                "inputs": {
                    "homeUrl": "http://www.n88dev.com",
                    "signupUrl": "http://www.n88dev.com/join",
                    "LoginUrl": "http://www.n88dev.com/login",
                    "tpId": "36",
                    "gameId": "0",
                    "CashierUrl": "http://www.n88dev.com/deposit",
                    "errorUrl": "https://error.0814media.net/404/index_en.html",
                    "tpGameType": "63",
                    "Host": "http://www.n88dev.com",
                    "ClientIP": "218.32.244.12",
                    "Token": token
                }
            }

            r = requests.post(self.tpsUrl + 'API/GotoGame', json = data)
            result = json.loads(r.text)
            self.assertEquals(result['errorCode'], 0)
            self.assertRegex(result['message'], 'https?:\/\/')

    def test_07_PT_LiveCasino_Login(self):

        token = self.__class__.token
        data = {
            "TpId": 27,
            "CustId": self.custId,
            "LangId": "en",
            "AppType": 1,
            "inputs": {
                "gameId": "0",
                "fun": "0",
                "gameType": "slots",
                "tpGameType": "48",
                "Host": "http://www.n88dev.com",
                "ClientIP": "218.32.244.12",
                "Token": token
            }
        }

        r = requests.post(self.tpsUrl + 'API/GotoGame', json = data)
        result = json.loads(r.text)
        self.assertEquals(result["errorCode"], 5003)

    def test_08_MG_LiveCasino_Login(self):

        token = self.__class__.token
        data = {
            "TpId": 34,
            "CustId": self.custId,
            "LangId": "en",
            "AppType": 1,
            "SiteId": 1,
            "inputs": {
                "homeUrl": "http://www.n88dev.com",
                "signupUrl": "http://www.n88dev.com/join",
                "LoginUrl": "http://www.n88dev.com/login",
                "tpId": "34",
                "gameId": "0",
                "CashierUrl": "http://www.n88dev.com/deposit",
                "errorUrl": "https://error.0814media.net/404/index_en.html",
                "tpGameType": "58",
                "Host": "http://www.n88dev.com",
                "ClientIP": "218.32.244.12",
                "Token": token
            }
        }

        r = requests.post(self.tpsUrl + 'API/GotoGame', json = data)
        result = json.loads(r.text)
        self.assertEquals(result['errorCode'], 0)
        self.assertRegex(result['message'], 'https?:\/\/')

    def test_09_DG_LiveCasino_Login(self):

        token = self.__class__.token
        data = {
            "TpId": 4,
            "CustId": self.custId,
            "LangId": "en",
            "AppType": 1,
            "SiteId": 1,
            "inputs": {
                "homeUrl": "http://www.n88dev.com",
                "signupUrl": "http://www.n88dev.com/join",
                "LoginUrl": "http://www.n88dev.com/login",
                "tpId": "4",
                "gameId": "4",
                "CashierUrl": "http://www.n88dev.com/deposit",
                "errorUrl": "https://error.0814media.net/404/index_en.html",
                "tpGameType": "10",
                "Host": "http://www.n88dev.com",
                "ClientIP": "218.32.244.12",
                "Token": token
            }
        }

        r = requests.post(self.tpsUrl + 'API/GotoGame', json = data)
        result = json.loads(r.text)
        self.assertEquals(result['errorCode'], 0)
        self.assertRegex(result['message'], 'https?:\/\/')

    def test_10_AE_LiveCasino_Login(self):

        token = self.__class__.token
        data = {
            "TpId": 15,
            "CustId": self.custId,
            "LangId": "en",
            "AppType": 1,
            "SiteId": 1,
            "inputs": {
                "homeUrl": "http://www.n88dev.com",
                "signupUrl": "http://www.n88dev.com/join",
                "LoginUrl": "http://www.n88dev.com/login",
                "tpId": "15",
                "gameId": "15",
                "CashierUrl": "http://www.n88dev.com/deposit",
                "errorUrl": "https://error.0814media.net/404/index_en.html",
                "tpGameType": "18",
                "Host": "http://www.n88dev.com",
                "ClientIP": "218.32.244.12",
                "Token": token
            }
        }

        r = requests.post(self.tpsUrl + 'API/GotoGame', json = data)
        result = json.loads(r.text)
        self.assertEquals(result["errorCode"], 0)
        self.assertRegex(result['message'], 'https?:\/\/')

    def test_11_SA_LiveCasino_Login(self):

        token = self.__class__.token
        data = {
            "TpId": 2,
            "CustId": self.custId,
            "LangId": "en",
            "AppType": 1,
            "SiteId": 1,
            "inputs": {
                "homeUrl": "http://www.n88dev.com",
                "signupUrl": "http://www.n88dev.com/join",
                "LoginUrl": "http://www.n88dev.com/login",
                "tpId": "2",
                "gameId": "2",
                "CashierUrl": "http://www.n88dev.com/deposit",
                "errorUrl": "https://error.0814media.net/404/index_en.html",
                "tpGameType": "9",
                "Host": "http://www.n88dev.com",
                "ClientIP": "218.32.244.12",
                "Token": token
            }
        }

        r = requests.post(self.tpsUrl + 'API/GotoGame', json = data)
        result = json.loads(r.text)
        self.assertEquals(result['errorCode'], 0)
        self.assertRegex(result['message'], 'https?:\/\/')

    def test_12_Allbet_LiveCasino_Login(self):

        token = self.__class__.token
        data = {
            "TpId": 12,
            "CustId": self.custId,
            "LangId": "en",
            "AppType": 1,
            "SiteId": 1,
            "inputs": {
                "homeUrl": "http://www.n88dev.com",
                "signupUrl": "http://www.n88dev.com/join",
                "LoginUrl": "http://www.n88dev.com/login",
                "tpId": "12",
                "gameId": "12",
                "CashierUrl": "http://www.n88dev.com/deposit",
                "errorUrl": "https://error.0814media.net/404/index_en.html",
                "tpGameType": "6",
                "Host": "http://www.n88dev.com",
                "ClientIP": "218.32.244.12",
                "Token": token
            }
        }

        r = requests.post(self.tpsUrl + 'API/GotoGame', json = data)
        result = json.loads(r.text)
        self.assertEquals(result['errorCode'], 0)
        self.assertRegex(result['message'], 'https?:\/\/')

    def test_13_AG_LiveCasino_Login(self):

        token = self.__class__.token
        data = {
            "TpId": 3,
            "CustId": self.custId,
            "LangId": "en",
            "AppType": 1,
            "SiteId": 1,
            "inputs": {
                "homeUrl": "http://www.n88dev.com",
                "signupUrl": "http://www.n88dev.com/join",
                "LoginUrl": "http://www.n88dev.com/login",
                "tpId": "3",
                "gameId": "3",
                "CashierUrl": "http://www.n88dev.com/deposit",
                "errorUrl": "https://error.0814media.net/404/index_en.html",
                "tpGameType": "8",
                "Host": "http://www.n88dev.com",
                "ClientIP": "218.32.244.12",
                "Balance": "0",
                "Token": token
            }
        }

        r = requests.post(self.tpsUrl + 'API/GotoGame', json = data)
        result = json.loads(r.text)
        self.assertEquals(result["errorCode"], 1001)

    def test_14_WM_LiveCasino_Login(self):

        token = self.__class__.token
        data = {
            "TpId": 20,
            "CustId": self.custId,
            "LangId": "en",
            "AppType": 1,
            "SiteId": 1,
            "inputs": {
                "homeUrl": "http://www.n88dev.com",
                "signupUrl": "http://www.n88dev.com/join",
                "LoginUrl": "http://www.n88dev.com/login",
                "tpId": "20",
                "gameId": "20",
                "CashierUrl": "http://www.n88dev.com/deposit",
                "errorUrl": "https://error.0814media.net/404/index_en.html",
                "tpGameType": "32",
                "Host": "http://www.n88dev.com",
                "ClientIP": "218.32.244.12",
                "Token": token
            }
        }

        r = requests.post(self.tpsUrl + 'API/GotoGame', json = data)
        result = json.loads(r.text)
        self.assertEquals(result['errorCode'], 9000)

    def test_15_eBet_LiveCasino_Login(self):

        token = self.__class__.token
        data = {
            "TpId": 18,
            "CustId": self.custId,
            "LangId": "en",
            "AppType": 1,
            "SiteId": 1,
            "inputs": {
                "homeUrl": "http://www.n88dev.com",
                "signupUrl": "http://www.n88dev.com/join",
                "LoginUrl": "http://www.n88dev.com/login",
                "tpId": "18",
                "gameId": "18",
                "CashierUrl": "http://www.n88dev.com/deposit",
                "errorUrl": "https://error.0814media.net/404/index_en.html",
                "tpGameType": "28",
                "Host": "http://www.n88dev.com",
                "ClientIP": "218.32.244.12",
                "Token": token
            }
        }

        r = requests.post(self.tpsUrl + 'API/GotoGame', json = data)
        result = json.loads(r.text)
        self.assertEquals(result['errorCode'], 9000)