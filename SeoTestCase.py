import unittest
import requests
import json

class SeoTestCase(unittest.TestCase):

    def setUp(self):
        self.url =  'https://www.n88dev.com/'

    def test_1_no_seo_domain(self):

        headers = {'Host': 'test.nova88test.com'}
        r = requests.post(self.url + 'api/Site/Seo', headers = headers)
        result = json.loads(r.text)
        self.assertIsNone(result["data"])

    def test_2_nova88bkk_seo(self):

        headers = {'Host': 'test.nova88bkk.com'}
        r = requests.post(self.url + 'api/Site/Seo', headers = headers)
        result = json.loads(r.text)
        title = "คาสิโนสด | คาสิโนสล็อต| คีโน | หวย | เดิมพันกีฬา | คาสิโนยิงปลา | Nova88 - เว็บไซต์เดิมพันออนไลน์และการพนันออนไลน์ที่เชื่อถือได้"
        meta = "Nova88 เป็นเว็บไซต์เดิมพันและการพนันออนไลน์ที่ดีที่สุดและน่าเชื่อถือที่สุดในเอเชีย เข้าร่วมและเล่นเกมกีฬา คาสิโนสด คาสิโนสล็อต ลอตเตอรี คีโน และเกมยิงปลา"
        self.assertEquals(title, result["data"]["title"])
        self.assertEquals(meta, result["data"]["meta"])

    def test_3_nova88bkk_GetMenuOfGames(self):

        headers = {'Host': 'test.nova88bkk.com'}
        r = requests.post(self.url + 'api/Site/GetMenuOfGames', headers = headers)
        result = json.loads(r.text)
        self.assertEquals(0, result["errorCode"])

    def test_4_nova88my5_seo(self):

        headers = {'Host': 'www.nova88my5.com'}
        r = requests.post(self.url + 'api/Site/Seo', headers = headers)
        result = json.loads(r.text)
        title = "Online Football Betting Malaysia | Online Live Sports Betting | Nova88  - The Trusted Online Casino Site"
        meta = "Looking for online football betting platform? Nova88 cover wide variety of online football betting and in play market on a monthly basis on sports. Download the App or place bets to support your favor team now!"
        self.assertEquals(title, result["data"]["title"])
        self.assertEquals(meta, result["data"]["meta"])

    def test_5_nova88my5_GetMenuOfGames(self):

        headers = {'Host': 'www.nova88my5.com'}
        r = requests.post(self.url + 'api/Site/GetMenuOfGames', headers = headers)
        result = json.loads(r.text)
        self.assertEquals(0, result["errorCode"])
