from re import match

from phonebookapp.phonebook import Phonebook

phonebook = Phonebook()

while True:
    main_menu = """\t\tWelcome to the Phonebook

    1) Add Contact
    2) Find Contact
    3) Edit Contact
    4) Delete Contact

    0) Exit"""
    print(main_menu)
    navigate = int(input("Enter your choice: "))
    match navigate:
        case 1:
            first_name = input("Enter your first name: ")
            last_name = input("Enter your last name: ")
            phone_number = input("Enter your phone number: ")

            try:
                phonebook.add_contact(first_name, last_name, phone_number)
                print("Contact added successfully")
            except ValueError:
                print("Contact not added")

        case 2:
            while True:
                find_menu = """\t\tFind Contact
                1) Find Contact via First Name
                2) Find Contact via Last Name
                3) Find Contact via Phone Number
                
                0) Back to main menu"""
                print(find_menu)
                navigate = int(input("Enter your choice: "))
                match navigate:
                    case 1:
                        first_name = input("Enter contact first name: ")
                        print(phonebook.find_contact_via_firstname(first_name))

                    case 2:
                        last_name = input("Enter contact last name: ")
                        print(phonebook.find_contact_via_lastname(last_name))

                    case 3:
                        phone = input("Enter contact phone number: ")
                        print(phonebook.find_contact_via_phonenumber(phone))

                    case 0:
                        break

                    case _:
                        print("That's not a valid choice")


        case 3:
            print("Edit Contact")
            full_name = input("Enter contact full name(firstName lastName): ")
            new_first_name = input("Enter new contact first name: ")
            new_last_name = input("Enter new contact last name: ")
            new_phone_number = input("Enter new contact phone number: ")
            try:
                phonebook.add_contact(new_first_name, new_last_name, new_phone_number)
                print("Contact Updated successfully")
            except ValueError:
                print("Contact not updated")

        case 4:
            print("Delete Contact")
            first_name = input("Enter contact first name: ")
            last_name = input("Enter contact last name: ")
            phone_number = input("Enter contact phone number: ")
            try:
                phonebook.delete_contact(first_name, last_name, phone_number)
                print("Contact deleted successfully")
            except ValueError:
                print("Contact not deleted")


        case 0: break

        case _:
            print("That's not a valid choice")