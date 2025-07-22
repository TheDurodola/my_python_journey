from phonebookapp.contact import Contact


class Phonebook():

    def __init__(self):
        self.__database = []


    def database_size(self):
        return len(self.__database)

    def add_contact(self, firstName, lastName, phoneNumber):
        self.__database.append(Contact(firstName, lastName, phoneNumber))