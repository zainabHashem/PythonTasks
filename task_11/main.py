# Title: Assignment 3
# Created by: Anas Ismail
# Date: May, 13th 2024

# Please don't change any part of the provided code. Only add new code.
# Please change the file name to be yourId_FirstName_LastName.py

# write your full name
NAME = "Zainab Hashem"
# write your id as a string
ID = "1110170685"

import sys, os
GRADING_MODE = False # only enable if you know what you are doing

if GRADING_MODE:
    sys.stdin = open('input.txt', 'r')

def init():
    s = "s ahmed ali, 01002271982\nmahmoud samir, 01119237865\nhend ibrahim, 01583637653\nmalak sami, 01112223333\nmalak mostafa, 01212223442\n"
    with open("phonebook.txt", "w") as f:
        f.write(s)


# colors 
# https://sentry.io/answers/print-colored-text-to-terminal-with-python/
RED = '\033[31m'
RESET = '\033[0m' # called to return to standard terminal text color
def red_font(s):
    return RED + str(s) + RESET


#....................................
#1)load func
def load(filename):
    #create dictionary 
    phonebook = {}
    try:
        f = open(filename, 'r')
        for line in f:
            #unbackge the name & phone num
            name, num = line.strip().split(',')
            #add name as key & phone num as value
            phonebook[name] = num
        f.close()
        return phonebook
    except FileNotFoundError:
        print(f"file {filename} not found")
        return {}

#....................................
#2)save func
def save(phonebook, filename):
    f = open(filename, 'w')
    for name in phonebook:
        num = phonebook[name]
        #write name & phone num in file
        f.write(f"{name},{num}\n")        
    f.close()
    print("saved successfully")

#....................................
#3)add func
def add(phonebook):
    #user insert name & phone num
    name = input("insert name: ")
    num = input("insert number: ")
    
    if name in phonebook:
        print(f"{name} aleady exist")
    else:
        phonebook[name] = num
        print(f"{name} added")

#....................................
#4)find func
def find(phonebook):
    #user insert name to find phone num
    name = input("insert name to find: ")
    if name in phonebook:
        print(f"{name} -> {phonebook[name]}")
    else:
        print(f"{name} not found")

#....................................
#5)update func
def update(phonebook):
    #user insert name to update phone num
    name = input("insert name to update: ")
    if name in phonebook:
        num = input("insert new number: ")
        phonebook[name] = num
        print(f"{name} updated")
    else:
        add = input(f"{name} not found \n do you want to add it? (y/n): ")
        if add == 'y':
            num = input("insert new number: ")
            phonebook[name] = num
            print(f"{name} added")
        else:
            print(f"{name} not updated")
            
#....................................
#6)delete func
def delete(phonebook):
    #delete the contact info of some name if it exists
    name = input("insert name to delete: ")
    if name in phonebook:
        del phonebook[name]
        print(f"{name} deleted")
    else:
        print(f"{name} not found")

#....................................
#7)view func
def view(phonebook):
    #dispaly all contacts
    print("contacts:")
    for name in phonebook:
        print(f"{name} -> {phonebook[name]}")
                
#....................................
#8)exit func
def exitP(phonebook):
    save(phonebook, "phonebook.txt")
    print("exiting program...")
    sys.exit()

#....................................
#9)menu func
def help():
    print(f"Press {red_font('e')} to exit")
    print(f"Press {red_font('a')} to add a contact")
    print(f"Press {red_font('d')} to delete a contact")
    print(f"Press {red_font('s')} to save data to file")
    print(f"Press {red_font('l')} to load data from file")  
    print(f"Press {red_font('v')} to view all your contacts")
    print(f"Press {red_font('f')} to find the phone number of a given name")
    print(f"Press {red_font('u')} to update the phone number of a given name")
    print(f"Press {red_font('h')} to show help message")

#....................................
#10)welcome func
def welcome():
    message = f"Welcome to {red_font(NAME)}'s phonebook app"
    n = len(message) - len(NAME)
    print("-"*n)
    print(message)
    print("-"*n)
    help()

#....................................
#11)main func
def main():
    if GRADING_MODE:
        init()

    # empty phonebook
    phonebook = {}

    welcome()
    while True:
        choice = input("> ").lower()
        if choice == "e":
            exitP(phonebook) 
        elif choice == "l":
            phonebook = load("phonebook.txt")
            print("Phonebook loaded successfully")
        elif choice == "s":
            save(phonebook, "phonebook.txt")
        elif choice == "a":
            add(phonebook)
        elif choice == "f":
            find(phonebook)
        elif choice == "u":
            update(phonebook)
        elif choice == "d":
            delete(phonebook)
        elif choice == "v":
            view(phonebook)
        elif choice == "h":
            help()
        else:
            print("invalid input.")
            help()

#....................................
#run the prgram
if __name__ == "__main__":
    main()






