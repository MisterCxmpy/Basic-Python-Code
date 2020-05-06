#Basic Password Gen Made With Python
#Password is "Password"
from os import system, name
import random
import time
import os
import getpass

char = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!£$%^&*"          # The character list used to generate the password

def masterPass():

    counter = 1
    masterPassword = getpass.getpass(prompt="Please enter the master password: ")       # GetPass has been used to prevent the password from showing
    while True:
        if counter == 3:
            print("Locked out")
            exit()
        elif masterPassword == "Password":
            time.sleep(1)
            print("Password successfully entered!")
            time.sleep(2)
            clear()
            options()
            break
        else:
            masterPassword = input("Wrong password, try again: ")
            time.sleep(0.5)
        counter += 1


f = 'password.txt'
file = open("password.txt", "a")
file.close()

def options():

    print("")
    print("Password Generator v2")
    option = input("""
Would you like to create a new password:
Would you like to view your current password list:
Would you like to clear your current password list:
Input [Create/View/Clear]: """)

    if option.capitalize() == "Create":
        create_Password()
    elif option.capitalize() == "View":
        open_Passwords()
    elif option.capitalize() == "Clear":
        clear_Passwords()
    else:
        print("Not valid responce")
        print("")
        time.sleep(2)
        clear()
        options()



def create_Password():
    password_length = int(input("Input a password length: "))
    site = input("Input the site: ")

    password = ""
    for l in range(password_length):
        password += random.choice(char)
    currentDirectory = os.getcwd()
    print("Your password has been saved under", currentDirectory, "- password.txt")
    file = open("password.txt", "a")
    file.write(password + ' | ' + site)
    file.write("\n")
    file.close()
    time.sleep(1.5)
    print("\n")
    input("Press ENTER to continue ")
    time.sleep(0.75)
    clear()
    options()

def open_Passwords():
    file = open("password.txt", "r")
    if os.stat(f).st_size ==0:
        time.sleep(1.5)
        print("Loading passwords...")
        time.sleep(1.5)
        print("You have no passwords.")
        time.sleep(1.5)
        print("\n")
        input("Press ENTER to continue ")
        time.sleep(0.75)
        clear()
        options()
    else:
        file_contents = file.read()
        time.sleep(1.5)
        print("Loading passwords...")
        time.sleep(1)
        print(file_contents)
        file.close()
        time.sleep(1.5)
        input("Press ENTER to continue ")
        time.sleep(0.75)
        clear()
        options()

def clear_Passwords():
    open('password.txt', 'w').close()
    time.sleep(1.5)
    print("Clearing passwords...")
    time.sleep(1)
    print("Passwords cleared.")
    time.sleep(1.5)
    print("\n")
    input("Press ENTER to continue ")
    time.sleep(0.75)
    clear()
    options()


def clear():
    if name == 'nt':
        _ = system('cls')

masterPass()
