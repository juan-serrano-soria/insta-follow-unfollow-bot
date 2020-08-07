from instapy import InstaPy

# account credentials
user = input("Instagram username: ")
psw = input("Instagram password: ")

# open session
session = InstaPy(username=user, password=psw, geckodriver_path='./driver/geckodriver')
session.login()

# close session
session.end()
