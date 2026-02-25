#Nicholas Terrazas and Devin Heinemann
#Lab 6
#02/23/2026

#Description: 

from contact import Contact
from check_input import get_int_range
import os

file_path = os.path.abspath("Lab6\\addresses.txt")

def read_file():
    """
    Reads contacts from addresses.txt, constructs Contact objects, 
    stores them in a list, sorts and returns the list.
    """
    contacts = []

    with open(file_path, "r") as f:
        # read lines
        lines = f.readlines()

    for line in lines:
        data = line.strip().split(",")
        contact = Contact(data[0], data[1], data[2], data[3], data[4], data[5])
        contacts.append(contact)

    #sort contacts by last name, then first name
    contacts.sort()
    f.close()
    return contacts


def write_file(contacts):
    """
    Writes all contacts back to the file using repr(contact).
    """
    # open file for writing
    with open(file_path, "w") as f:
        for contact in contacts:
            f.write(repr(contact) + "\n")
    f.close()



def get_menu_choice():
    """
    Displays main menu and returns validated user choice.
    """
    print("Rolodex Menu:")
    print("1. Display Contacts")
    print("2. Add Contact")
    print("3. Search Contacts")
    print("4. Modify Contact")
    print("5. Save and Quit")

    choice = get_int_range(">", 1, 5)
    return choice


def modify_contact(cont):
    """
    Allows user to modify a contact's attributes until they choose to save.
    """
    choice = 0

    while choice != 7:
        print("Modify Menu:")
        print("1. First name")
        print("2. Last name")
        print("3. Phone")
        print("4. Address")
        print("5. City")
        print("6. Zip")
        print("7. Save")

        choice = get_int_range(">", 1, 7)

        if choice == 1:
            # prompt for new first name
            new_first = input("Enter new first name: ")
            cont.set_first_name(new_first)
        if choice == 2:
            # prompt for new last name
            new_last = input("Enter new last name: ")
            cont.set_last_name(new_last)
        if choice == 3:
            #prompt for new phone number
            new_phone = input("Enter new phone number: ")
            cont.set_phone(new_phone)
        if choice == 4:
            #prompt for new address
            new_address = input("Enter new address: ")
            cont.set_address(new_address)
        if choice == 5:
            #prompt for new city
            new_city = input("Enter new city: ")
            cont.set_city(new_city)
        if choice == 6:
            new_zip = input("Enter new zip code: ")
            cont.set_zip(new_zip)


#Helper functions for main menu options
def display_contacts(contacts):
    """Displays number of contacts and enumerated list."""
    print(f"Number of contacts: {len(contacts)}" + "\n")
    for i, contact in enumerate(contacts, 1):
        print(f"{i}. {contact}")

def add_contact(contacts):
    """Prompts user for contact info and adds to list."""
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    phone = input("Enter phone number: ")
    address = input("Enter address: ")
    city = input("Enter city: ")
    zip_code = input("Enter zip code: ")

    new_contact = Contact(first_name, last_name, phone, address, city, zip_code)
    contacts.append(new_contact)


def search_contacts(contacts):
    """Search by last name or zip and display matches."""
    search_type = get_int_range("Search by: \n 1. Last Name\n 2. Zip Code \n >", 1, 2)

    if search_type == 1:
        last_name = input("Enter last name to search: ")
        matches = [contact for contact in contacts if contact._l_name == last_name]
    else:
        zip_code = input("Enter zip code to search: ")
        matches = [contact for contact in contacts if contact._zip == zip_code]

    if matches:
        print(f"Found {len(matches)} matching contacts:")
        for contact in matches:
            print(contact)
    else:
        print("No matching contacts found.")


def find_contact(contacts, first, last):
    """
    Returns matching contact object or None.
    """
    for contact in contacts:
        if contact._f_name == first and contact._l_name == last:
            return contact
    return None

def main():
    contacts = read_file()

    done = False
    while not done:

        choice = get_menu_choice()

        if choice == 1:
            display_contacts(contacts)

        elif choice == 2:
            add_contact(contacts)
            contacts.sort()

        elif choice == 3:
            search_contacts(contacts)

        elif choice == 4:
            #prompt for name
            first = input("Enter first name of contact to modify: ")
            last = input("Enter last name of contact to modify: ")

            cont = find_contact(contacts, first, last)
            if cont:
                modify_contact(cont)
                contacts.sort()
            else:
                print("Contact not found.")

        elif choice == 5:
            print("Saving File...")
            write_file(contacts)
            print("Ending Program")
            done = True

if __name__ == "__main__":
    main()