from instapy import InstaPy
from getpass import getpass
import sys

# argv control
if (len(sys.argv) == 1):
    print("Please, input the file to read from as an argument")
    sys.exit(1)
if(len(sys.argv) > 2):
    print("Incorrect number of arguments, you can only read from one file")
    sys.exit(1)

# account credentials
user = input("Instagram username: ")
psw = getpass("Instagram password: ")

# open session
session = InstaPy(username=user, password=psw, geckodriver_path='./driver/geckodriver')
session.login()

# open text file and read it into a list
f = open(str(sys.argv[1]), "r")
accounts = f.read().splitlines()
f.close()

# accounts that won't be unfollowed in any case
friends = []
session.set_dont_include(friends)

# unfollow the accounts that don't follow you back from that accounts list
session.unfollow_users(amount=len(accounts), custom_list_enabled=True, custom_list=accounts, custom_list_param="nonfollowers", style="RANDOM", unfollow_after=0, sleep_delay=600)

# close session
session.end()
