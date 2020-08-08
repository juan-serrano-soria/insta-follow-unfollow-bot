from instapy import InstaPy
from getpass import getpass

# account credentials
user = input("Instagram username: ")
psw = getpass("Instagram password: ")

# open session
session = InstaPy(username=user, password=psw, geckodriver_path='./driver/geckodriver')
session.login()

# open text file and read it into a list
f = open("sample_accounts_followers.txt", "r")
accounts = f.read().splitlines()
f.close()

# follow these accounts, without ignoring private accounts
session.set_skip_users(skip_private=True, private_percentage=0)
follow_by_list(followlist=accounts, times=1, sleep_delay=600, interact=False)

# close session
session.end()
