from Classes import *

username = input()
password = input()
account = input()

insta_bot = InstaBot(username, password, account)

data = insta_bot.ff_comparator()

print(data)

for k, v in data.items():
    with open(k, "a") as f:
        for insta_account in v:
            f.write(f"{insta_account}\n")
