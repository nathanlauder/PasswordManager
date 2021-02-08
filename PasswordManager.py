# PasswordManager.py
# a python script to manage my passwords that way they will 
# be more secure and I can just copy and paste them
# Nathan Lauder

# I am also using this project as an introduction to hash tables in python
# the main function will be an infinite loop where it can only be hit by pressing "q" for quit
from random import randrange
combos = {}

# take a service and generated password and put them into the dictionary
def insertPair(service, password):
    combos[service] = password

# generates a random password from the general allowed characters for passwords
def generatePassword(passLen):
    possibleChars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%&*"
    password = ""
    for i in range(passLen):
        password += possibleChars[randrange(68)]
    return password

# finds the password where the service parameter is the key to the dictionary
def findPassword(service):
    return combos[service]

# prints all the password pairs
def showAll():
    keyList = combos.items()
    for pair in keyList:
       print(pair[0]+"->"+pair[1])

# main function will have a sentinel loop with possible commands to add 
# a service and password, find the password for a service, or quit the loop
def main():
    answer = ""
    while True:
        print("\nq: quit" + "\n" + "np: new password" + "\n" + "fp: find password")
        answer = input("What action do you wanna perform\n")
        
        if answer == 'q':
            break
        # put a new password into the map with new service
        elif answer == "np":
            newService = input("What is the service?  ")
            passLen = int(input("How many characters for the service? "))
            passForService = generatePassword(passLen)
            insertPair(newService, passForService)
            
        # find a password already in the dictionary
        elif answer == "fp":
            existingService = input("Which service do you need to find the password for? ")
            print(findPassword(existingService))

        elif answer == "show":
            showAll()
        # start the loop over if the command isn't known or there is a typo
        else:
            print("command not recognized, please try again")

main()

if __name__ == "__main__":
    main()