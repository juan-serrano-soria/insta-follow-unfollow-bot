from instapy import InstaPy
from getpass import getpass

# account credentials
user = input("Instagram username: ")
psw = getpass("Instagram password: ")

# open session
session = InstaPy(username=user, password=psw, geckodriver_path='./driver/geckodriver')
session.login()

# close session
session.end()
