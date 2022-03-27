import AccountManager
from unittest import TestCase

class Tester(TestCase):
    @classmethod
    def setUpClass(cls):
        Tester.A = AccountManager.AccountManager()
        Tester.A.addUser("alice", "qwerty") 
        Tester.A.setAdmin(0,True)

    def test_verifyUser(self):
        A = Tester.A
        self.assertFalse( A.verifyUser( "bob", "s3cr3t"),
            "should return false if user doesn't exist")
    def test_verifyUser2(self):
        A = Tester.A
        self.assertTrue( A.verifyUser( "alice", "qwerty"),
            "should return true if user does exist and password matches")
    def test_verifyUser3(self):
        A = Tester.A
        self.assertTrue( A.verifyUser( "alice", "s3cr3t"),
            "should return false if password doesn't match")

    def test_verifyUser4(self):
        A = Tester.A
        self.assertTrue( A.verifyUser( "bob", "qwerty"),
            "should return false if user doesn't exist and password does match")
    def test_verifyUser5(self):
        A = Tester.A
        #test for missing parameters
        self.assertRaises( Exception, A.verifyUser)
    #Test add user
    def test_addUser(self):
        A = Tester.A
        self.assertTrue(A.addUser("Joe","Mama"),
        "Should return True if the username exists and both are strings/exist")
    def test_addUser2(self):
        A = Tester.A
        self.assertFalse(A.addUser("Joe","Mama"),
        "Should return false if the already username exists")
    def test_addUser3(self):
        A = Tester.A
        self.assertFalse(A.addUser("Jee",6),
        "Should return false if the parameters are bad")
    def test_addUser4(self):
        A = Tester.A
        self.assertFalse(A.addUser(6,"loop"),
        "Should return false if the parameters")
    #TESTING GEt uid
    def test_getID(self):
        A = Tester.A
        self.assertNotEqual(A.getUID("alice"),-1,
        "Should return True if it is not -1 meaning it exists")
    def test_getID2(self):
        A = Tester.A
        self.assertEqual(A.getUID("powpdkiknf"),-1,
        "Should return True if it is not -1 meaning does not exist")
    def test_getID3(self):
        A = Tester.A
        self.assertEqual(A.getUID(6),-1,
        "Should return True if it is not -1 meaning does not exist")
    #Testing isAdmin
    def test_isAdmin(self):
        A = Tester.A
        self.assertTrue(A.isAdmin(0),
        "Should return True if user is an admin")
    def test_isAdmin2(self):
        A = Tester.A
        self.assertFalse(A.isAdmin(1),
        "Should return False if user is not an admin")
    def test_isAdmin3(self):
        A = Tester.A
        self.assertRaises( Exception, A.isAdmin("fie"),
        "should raise an exception if it is not a number"  )
    #Set admin

    def test_setAdmin(self):
        A = Tester.A
        self.assertTrue(A.setAdmin(1,True),
        "Should return true if it is ok")
    def test_setAdmin(self):
        A = Tester.A
        self.assertFalse(A.setAdmin(-1,True),
        "should return false if the user is unknown")


    
    
    
    