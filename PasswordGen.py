# Basic Password Gen Made With Python

import random
import sys
import time
import os

char = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!£$%^&*"

print("Basic password generator made with Python")
time.sleep(0.5)
password_length = int(input("Input a password length: "))
site = input("Input the site: ")

password = ""
for l in range(password_length):
    password += random.choice(char)
currentDirectory = os.getcwd()
print("Your password has been saved under", currentDirectory, "- password.txt")
file = open("password.txt","a")
file.write(password + ' | ' + site)
file.write("\n")
file.close()
