from http.client import FORBIDDEN
from unittest import TestCase
import urllib
import http
import django.test
import AccountManager
import tests    .utils as utils
class T(TestCase):

    def setUp(self):
        AccountManager.clear()

    #def test_register1(self):
    #    c = django.test.Client()
    #    resp = c.post("/register")
    #    self.assertEqual(resp.status_code,http.HTTPStatus.OK)
    def test_register2(self):
        resp = utils.createAccount("Accountant","Poop")
        self.assertEqual(resp.status_code,http.HTTPStatus.OK)
    def test_registerNoDupe(self):
        resp = utils.createAccount("Tent@epic.com","pee")
        self.assertEqual(resp.status_code,http.HTTPStatus.OK)
        resp = utils.createAccount("Tent@epic.com","pee")
        self.assertEqual(resp.status_code,http.HTTPStatus.BAD_REQUEST)
    def test_registerBlankUname(self):
        print("meme")
        resp = utils.createAccount("","Poop")
        self.assertEqual(resp.status_code,http.HTTPStatus.BAD_REQUEST)
    def test_registerBlankPass(self):
        print("lol")
        resp = utils.createAccount("Memes","")
        self.assertEqual(resp.status_code,http.HTTPStatus.BAD_REQUEST)
    def test_registerNoPass(self):
        c = django.test.Client()
        resp = c.post("/register",{"username":"uname"})
        self.assertEqual(resp.status_code,http.HTTPStatus.BAD_REQUEST)
    def test_registerNoUname(self):
        c = django.test.Client()
        resp = c.post("/register",{"password":"me"})
        self.assertEqual(resp.status_code,http.HTTPStatus.BAD_REQUEST)