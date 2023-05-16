import json
fileName = 'accounts.json'
class Account:
    def __init__(self):
        self.username = 'admin'
        self.password = 'admin'
    def make_account(self):
        while True:
            self.username = input('Enter username: ')
            if self.username in accountDict:
                print('Username taken. Choose another one.')
            else:
                self.password = input('Enter password: ')
                break
        accountDict[self.username] = self.password
        with open(fileName, 'w') as f:
            json.dump(accountDict, f)
    def log_in(self, username, password):
        try:
            with open(fileName) as f:
                accounts = json.load(f)
        except:
            raise FileNotFoundError('The Passwords file not found. ')
        else:
            if username in accounts and accounts[username] == password or \
                    username == self.username and password == self.password:
                print(f'Welcome back, {username}')
            else:
                print('Wrong username or password. Try again')

accountDict = {}
try:
    with open(fileName) as f:
        accountDict = json.load(f)
except:
    print('No account exist. Make an account:')
    firstUser = Account()
    firstUser.make_account()
else:
    pass
user1 = Account()
user1.make_account()
nInput = input('Username: ')
pInput = input('Password: ')
user1.log_in(nInput, pInput)






