# 1. Name:
#      -Michael Johnson-
# 2. Assignment Name:
#      Lab 02: Authentication
# 3. Assignment Description:
#      -This program reads usernames and passwords from a JSON file and prompts the user to input their credentials. 
#       It checks the case-sensitive username and password for authentication, and informs the user if they are authorized. 
#       The program loops until the user chooses to exit.-
# 4. What was the hardest part? Be as specific as possible.
#      -The hardest part of this project for me was figuring out how to correctly set up and use the index to match the username with the 
#       corresponding password, especially since I’m a little rusty with Python. It took me a bit of time to remember how to get the index from 
#       the list of usernames and use that same index to compare the password at the same position in the passwords list. Once I got that sorted 
#       out, though, the rest of the project was fairly simple and straightforward. The logic for checking the username and password and then looping 
#       until the user wants to stop was easy to implement after I worked through the indexing part.-
# 5. How long did it take for you to complete the assignment?
#      -total time in hours including reading the assignment and submitting the program-
#      including the reading, and everything, about 4 hours. 



import json

try:
    with open('lab2\\Lab02.json', 'r') as file:
        data = json.load(file)
except FileNotFoundError:
    print("Unable to open file Lab02.json.")
    exit()

usernames = data.get('username', [])
passwords = data.get('password', [])

while True:
    username_input = input("Please enter your username: ")
    password_input = input("Please enter your password: ")

    if username_input in usernames:
        index = usernames.index(username_input)
        if passwords[index] == password_input:
            print("You are authenticated!")
        else:
            print("You are not authorized to use the system.")
    else:
        print("You are not authorized to use the system.")

    try_again = input("Do you want to try again? (yes/no): ").lower()
    if try_again != 'yes':
        print("Exiting the program.")
        break

