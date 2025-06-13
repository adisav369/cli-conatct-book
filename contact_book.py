import json
import os

contact_file = "contacts.json"

def load_contacts():
    if not os.path.exists(contact_file):
        return {}
    try:
        with open(contact_file, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        # File exists but is empty or invalid
        return {}

def save_contacts(data):
    with open(contact_file, "w") as file:
        json.dump(data, file, indent=4)

def add_contacts():
    contacts = load_contacts()

    name = input("enter the name of the contact: ").strip()

    if name in contacts:
        print(f"{name} already exists in the contact list.")
        return
    
    phone = input("enter the phone number: ").strip()
    email = input("enter the email address: ").strip()
    address = input("enter the address: ").strip()

    contacts[name] = {
        "phone" : phone,
        "email_address" : email,
        "address" : address
    }

    save_contacts(contacts)
    print(f"contact {name} is saved to list successfully!")

def view_contacts():
    contacts = load_contacts()

    if not contacts:
        print("no contacts available in the contact list \n")
        return
    
    for name, info in contacts.items():
        print(f"name : {name}")
        print(f"phone number: {info['phone']}")
        print(f"email: {info['email_address']}")
        print(f"address: {info['address']}")
        print("-"*30)
def search_contacts():
    contacts = load_contacts()

    keyword = input("enter the name or phone number you want to search: ").strip().lower()

    found = False
    for name, info in contacts.items():
        if keyword in name.lower() or keyword in info['phone']:
            print(f"name: {name}")
            print(f"Phone number: {info['phone']}")
            print(f"email: {info['email_address']}")
            print(f"address: {info['address']}")
            print("-"*30)
            found = True
    if not found:
        print("No matching contact found \n")

def update_contacts():
    contacts = load_contacts()

    name = input("enter the name of the contact you want to update: ").strip().lower()

    if name not in contacts:
        print("no contact found \n")
        return
    print("if you dont want to update any item leave it blank to keep the current value \n")

    phone = input(f"New phone {contacts[name]['phone']}: ")
    email_address = input(f"New emai_address {contacts[name]['email_address']}: ")
    address = input(f"New address {contacts[name]['address']}: ")

    if phone:
        contacts[name]['phone'] = phone
    if email_address:
        contacts[name]['email_address'] = email_address
    if address:
        contacts[name]['address'] = address
    
    save_contacts(contacts)
    print("contact updated successfully \n")

def delete_contacts():
    contacts = load_contacts()
    name = input("enter the name of the contact you want to delete: ").strip().lower()

    if name not in contacts:
        print(f"contact not found with this name {name} \n")
        return
    confirm = input(f"are you sure do you want to delete this {name} contact enter (Y/N): ").strip().lower()

    if confirm == 'y':
        del contacts[name]
        save_contacts(contacts)
        print("contact deleted successfully")

    else:
        print("deletion cancelled \n")