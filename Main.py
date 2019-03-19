import random
import string
password_list = []
def new_password():
    website = input("What is the website: ")
    username = input("What is the username: ")
    password = input("What is the pasword: ")
    if password == "random":
        while True:
            N = int(input("How long do you want? "))
            if N < 8:
                print("Please try again: ")
                continue
            else:
                random_password = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(N))
                print(f"This is your random password: {random_password}")
                password = random_password
                break
    else:
        pass
    
    website_entry = dict([("website", website),("username", username),("password", password)])

    password_list.append(website_entry)
    print(password_list)
def find_password():
    what_website_password = input("What website's password are you trying to find? ")
    for entry in password_list:
        if entry["website"] == what_website_password:
            print(entry["username"])
            print(entry["password"])
            break
    print("Website does not exist!!!")
while True:
    print("""Hello welcome back
          just to make sure you remember we're dropping the commands as a refresher
          show: shows your password for a specific website
          add: Allows you to add extra website info
          """)
    option = input("What is it you would like to do? ")
    if option == "add":
        new_password()
    elif option == "show":
        find_password()
    else:
        print("Please try again correctly: ")
