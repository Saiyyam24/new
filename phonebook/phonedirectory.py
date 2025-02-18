import os
import json

FILE_NAME = "contacts.json"

# Create a dictionary to store the contacts
if os.path.exists(FILE_NAME):
    with open(FILE_NAME, 'r') as file:
        contacts = json.load(file)
else:
    contacts = {}

def save_contacts():
    with open(FILE_NAME, 'w') as file:
        json.dump(contacts,file,indent=4)
while  True:

    value = input("what you want to do create/read/update/delete/exit:").strip().lower()
    if value == "create":
        name = input("Enter name: ").strip().capitalize()
        number = input("Enter number: ").strip() 
        contacts[name] = number
        save_contacts()
    elif value == "read":
        name = input("Enter name: ").strip().capitalize()
        if name in contacts:
            print(contacts[name])
        else:
            print("No contact found")
    elif value == "update":
        name = input("Enter name: ").strip().capitalize()
        if name in contacts:
            number = input("Enter the number: ").strip()
            contacts[name] = number
        else:
            print ("no contact found")
        save_contacts()
    elif value == "delete":
        name = input("Enter the name: ").strip().capitalize()
        if name in contacts:
            del(contacts[name])
        else:
            print("no contact found") 
        save_contacts()                  
    elif value == "exit":
        break        
    else:
        print("invalid input")
