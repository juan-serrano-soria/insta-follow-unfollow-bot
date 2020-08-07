from instapy import InstaPy

# read the accounts from a file into a list
f = open("sample_accounts.txt", "r")
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
f = open("sample_accounts_followers.txt", "w")

for account in followers_no_duplicates:
    f.write(account + '\n')

f.close()