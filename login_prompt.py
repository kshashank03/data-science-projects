import os
import pandas as pd

dir_path = os.path.dirname(os.path.realpath(__file__))

temp_username = ["user1", "user2", "user3"]
temp_password = ["password1", "password2", "password3"]

login_information = pd.DataFrame(data=zip(temp_username, temp_password), 
                                columns=["usernames", "passwords"])

login_information.to_csv(dir_path + "/login_information.csv", index=False, header=True)



print("Welcome to the login screen.\nPlease input a username")
username = input()

login_information_import = pd.read_csv(dir_path + "/login_information.csv")

match = login_information_import[login_information_import["usernames"] == username].index.tolist()

while match == []:
    print("Please enter a valid username")
    username = input()
    match = login_information_import[login_information_import["usernames"] == username].index.tolist()
    if match != []:
        break

print("Please enter a password")
password = input()

match_str = " ".join(map(str, match))
match_int = int(match_str)
while str(login_information_import.passwords.iloc[match_int]) != password:
    print("Wrong password, try again")
    password = input()
    if str(login_information_import.passwords.iloc[match_int]) == password:
        break

print("Welcome")

os.remove(dir_path + "/login_information.csv")