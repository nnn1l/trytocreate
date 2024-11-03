from ur_11_dz.task2_ur11 import*

print("Welcome to a PhoneBook messenger! Here you can add and delete phone numbers, search phone numbers and also update information about phone numbers.\nTo do it just enter...\n1 - Add new phone number\n2 - Update\n3 - Search\n4 - Delete\n5 - Exit")

while True:
    action = input("Enter what would you like to do: ")
    if action == "1":
        new_entry(input("Enter a phone number: "), input("Enter a first name: "),input("Enter a last name: "), input("Enter an address: "))
    elif action == "2":
        update_record(input("Enter a phone number: "), input("Enter a first name: "), input("Enter a last name: "), input("Enter an address: "))
    elif action == "3":
        search(input("You are searching parameter.. : "), input("Enter an information: "))
    elif action == "4":
        delete_record(input("Enter a phone number: "))
    elif action == "5":
        exiting()