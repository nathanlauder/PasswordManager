# PasswordManager.py
# a python script to manage my passwords that way they will 
# be more secure and I can just copy and paste them
# Nathan Lauder

# I am also using this project as an introduction to hash tables in python
# the main function will be an infinite loop where it can only be hit by pressing "q" for quit
from random import randrange
combos =  {}

def main():
    answer = ""
    while answer != "q":
        print("\nq: quit" + "\n" + "np: new password" + "\n" + "fp: find password")
        answer = input("What action do you wanna perform\n")
        
        # put a new password into the map
        if answer == "np":
            service = input("What is the service?  ")
            passForService = generatePassword()
            insertPair(service, passForService)

        # find a password already in the map
        elif answer == "fp":
            stuffff
#main()
# def addPass(service, password):

def insertPair(service, password):
    combos[service] = password

def showCombos():
    print(combos)

def generatePassword():
    possibleChars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%&*"
    password = ""
    for i in range(12):
        password += possibleChars[randrange(68)]
    return password
generatePassword()