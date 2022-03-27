import django.test

def createAccount(uname,pw):
        c = django.test.Client()
        resp = c.post("/register",
            {
                "username":uname,
                "password":pw
            }
        )
        return resp