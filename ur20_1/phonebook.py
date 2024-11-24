import json

json_name = "phonebook_json.json"

with open(json_name, 'r+') as json_file:
    phonebook = json.loads(json_file.read())

def new_entry(phone_number, first_name, last_name, address):
    phonebook[phone_number] = {"phone_number" : phone_number, "first_name" : first_name,
                              "last_name" : last_name, "address" : address}
    return phonebook[phone_number]["first_name"]


def search(*args):
    x = 0
    all_contacts = list(phonebook.values())
    try:
        if (args[0].lower() != "full name" and args[0].lower() != "first name"
            and args[0].lower() != "last name" and args[0].lower() != "address" and args[0].lower() != "phone number"):
            print(f"You wrote a parameter {args[0]}, there is no parameters named like this.")
        while x < len(all_contacts):
            if all_contacts[x][args[0].replace(" ", "_")].lower() == args[1].lower():
                print(f"{all_contacts[x]["first_name"]} {all_contacts[x]["last_name"]} - {all_contacts[x]['phone_number']}")
                return all_contacts[x]["first_name"], all_contacts[x]["last_name"], all_contacts[x]["phone_number"]
            x += 1
    except KeyError:
        print("No information found")


def delete_record(phone_number):
    if phone_number in phonebook:
        print(f'{phonebook[phone_number]["first_name"]} {phonebook[phone_number]["last_name"]}`s phone number deleted')
        del phonebook[phone_number]
    elif phone_number not in phonebook:
        print("No information found")


def update_record(phone_number, first_name, last_name, address):
    if phone_number in phonebook:
        phonebook[phone_number] = {"phone_number" : phone_number, "first_name" : first_name,
                              "last_name" : last_name, "address" : address}
    elif phone_number not in phonebook:
        print("No information found")


def exiting():
    with open(json_name, 'w+') as json_write:
        json.dump(phonebook, json_write)
    print("Exiting...")
    exit()
