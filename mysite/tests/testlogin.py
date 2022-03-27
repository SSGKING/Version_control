import user
import django.test
from unittest import TestCase
import http
import tests.utils as utils
class T(TestCase):


    def test_notLoggedIn(self):
        c = django.test.Client()
        resp = c.get("/who")
        self.assertEqual("",resp.content.decode())
    def test_registerAndLogin(self):
        resp = utils.createAccount("Bob@example.com","secret")
        self.assertEqual(resp.status_code,http.HTTPStatus.OK)
        uname = resp.client.get("/who").content.decode()
        self.assertEqual(uname,"Bob@example.com")
    def test_copylogin(self):
        resp = utils.createAccount("Bobby@example.com","secret")
        self.assertEqual(resp.status_code,http.HTTPStatus.OK)

        resp = utils.createAccount("Bobby@example.com","secret")
        self.assertNotEqual(resp.status_code,http.HTTPStatus.OK)
        


        
