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

# generates a random password from lowercase, caps, numbers and some symbols
def generatePassword():
    possibleChars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%&*"
    password = ""
    for i in range(12):
        password += possibleChars[randrange(68)]
    return password

# finds the password where the service parameter is the key to the dictionary
def findPassword(service):
    return combos[service]

# prints all the password pairs
# can be used if implemented
#def showCombos():
 #   print(combos)

# main function will have a sentinel loop with possible commands to add 
# a service and password, find the password for a service, or quit the loop
def main():
    answer = ""
    while answer != "q":
        print("\nq: quit" + "\n" + "np: new password" + "\n" + "fp: find password")
        answer = input("What action do you wanna perform\n")
        
        # put a new password into the map with new service
        if answer == "np":
            newService = input("What is the service?  ")
            passForService = generatePassword()
            insertPair(newService, passForService)
            
        # find a password already in the dictionary
        elif answer == "fp":
            existingService = input("Which service do you need to find the password for? ")
            print(findPassword(existingService))

        # start the loop over if the command isn't known or there is a typo
        else:
            print("command not recognized, please try again")

main()

if __name__ == "__main__":
    main()