from instapy import InstaPy
import sys

# argv control
if (len(sys.argv) == 1):
    print("Please, input the file to read from and the file to write to as arguments")
    sys.exit(1)
if(len(sys.argv) > 3):
    print("Incorrect number of arguments, you must provide only two arguments")
    sys.exit(1)

# read the accounts from a file into a list
f = open(str(sys.argv[1]), "r")
accounts_list = f.read().splitlines()
f.close()

followers = []


# account credentials
user = input("Instagram username: ")
psw = getpass("Instagram password: ")

session = InstaPy(username=user, password=psw, geckodriver_path='./geckodriver')
session.login()

# grab followers of each account in our list and put them into a new list
for account in accounts_list:
    followers +=  session.grab_followers(username=account, amount="full", live_match=True, store_locally=False)


session.end()

# remove duplicates
followers_no_duplicates = list(set(followers))


# write list into a file
f = open(str(sys.argv[1]), "w")

for account in followers_no_duplicates:
    f.write(account + '\n')

f.close()