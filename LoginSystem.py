from csv import writer
import csv
import pandas as pd
import os
import sys

abspath = os.path.abspath(sys.argv[0])
dname = os.path.dirname(abspath)
os.chdir(dname)

if os.path.exists("Accounts.csv"):
    pass
else:
    with open("Accounts.csv", 'a+', newline='') as f:
        f.write("Username,Password")
        f.write("\n")

col_list = ["Username", "Password"]
df = pd.read_csv("Accounts.csv", usecols=col_list)
clear = lambda: os.system('cls')

def append_list_as_row(file_name, list_of_elem):
    with open(file_name, 'a+', newline='') as write_obj:
        csv_writer = writer(write_obj)
        csv_writer.writerow(list_of_elem)

def Select():
    global selection
    selection = int(input("""
Select your action.
Sign In {1}
Create Account {2}
Exit {3}
"""))

    while selection not in [1, 2, 3]:
        print("That is not an option")
        Select()
    if selection == 1:
        SignIn()
    elif selection == 2:
        CreateAccount()
    else:
        exit()

def SignIn():
    clear()
    userList = []
    with open("Accounts.csv") as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            userList.append(row[0])

    passList = []
    with open("Accounts.csv") as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            passList.append(row[1])

    username = input("Enter username: ")
    if username in userList:
        print("Username found!")
        password = input("Enter Password: ")
        if password in passList:
            clear()
            print("Password found!")
            print("User signed in!")
        else:
            clear()
            print("Password incorrect!")
            SignIn()
    else:
        clear()
        print("Username not found!")
        SignIn()

def CreateAccount():
    userList = []
    with open("Accounts.csv") as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            userList.append(row[0])

    username = input("Enter username: ")
    if username in userList:
        clear()
        print("Username already taken!")
        CreateAccount()
    else:
        password = input("Enter password: ")
        UserSet = [username, password]
        append_list_as_row("Accounts.csv", UserSet)
        clear()
        Select()

Select()