from contact_book import add_contacts
from contact_book import view_contacts, search_contacts, update_contacts,delete_contacts

def main():
    while True:
        print("CLI contact list project!")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("choose your option by entering a value from (1-6): ").strip()

        if choice == "1":
            add_contacts()
        elif choice == "2":
            print(f"you entered the value: {choice}")
            view_contacts()
        elif choice == "3":
            print(f"you entered the value: {choice}")
            search_contacts()
        elif choice == "4":
            print(f"you entered the value: {choice}")
            update_contacts()
        elif choice == "5":
            print(f"you entered the value: {choice}")
            delete_contacts()
        elif choice == "6":
            print(f"you entered the value: {choice} \n")
            print("application exit successfully, see you later bye!\n")
            return
        else:
            print("Enter the valid input")
if __name__ == "__main__":  
    main()