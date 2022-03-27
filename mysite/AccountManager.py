class AccountError(Exception):
    def __init__(self,reason):
        super().__init__(reason)

accounts = {}

class Account:
    def __init__(self,username,password):
        self.username = username
        self.password = password



def addAccount(username,password):
    if username == None:
        raise AccountError("Username Not Given")
    if username in accounts:
        raise AccountError("Username Already exists")
    if len(username.strip()) == 0:
        print("check")
        raise AccountError("Username Is Empty")
    if password == None:
        raise AccountError("Password Not Given")
    if len(password.strip()) == 0:
        raise AccountError("Password Is Empty")
    u = Account(username,password)
    accounts[username] = u


def clear():
    global accounts
    accounts = {}