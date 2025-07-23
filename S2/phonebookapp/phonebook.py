from phonebookapp.contact import Contact


class Phonebook():

    def __init__(self):
        self.__database = []


    def database_size(self):
        return len(self.__database)

    def add_contact(self, firstName, lastName, phoneNumber):
        self.__database.append(Contact(firstName, lastName, phoneNumber))

    def delete_contact(self, firstname, lastname, number):
        for contact in self.__database:
            if contact.get_firstname == firstname and contact.get_lastname == lastname and contact.get_phonenumber == number:
                self.__database.remove(contact)
                break

    def find_contact_via_firstname(self, firstname):
        for contact in self.__database:
            if contact.get_firstname == firstname:
                return contact.get_firstname, contact.get_lastname, contact.get_phonenumber
        return None

    def find_contact_via_lastname(self, lastname):
        for contact in self.__database:
            if contact.get_lastname == lastname:
                return contact.get_firstname, contact.get_lastname, contact.get_phonenumber
        return None

    def find_contact_via_phonenumber(self, number):
        for contact in self.__database:
            if contact.get_phonenumber == number:
                return contact.get_firstname, contact.get_lastname, contact.get_phonenumber
        return None

    def edit_contact(self, old_name, new_first_name, new_last_name, new_phone_number):
        for contact in self.__database:
            if contact.get_firstname+ " "+ contact.get_lastname == old_name:
                contact.set_firstname(new_first_name)
                contact.set_lastname(new_last_name)
                contact.set_phonenumber(new_phone_number)
                return
