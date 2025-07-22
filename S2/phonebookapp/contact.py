
class Contact:
    def __init__(self, firstName, lastName, phoneNumber):
        self.__validateinput(firstName, lastName, phoneNumber)
        self._firstName = firstName
        self._lastName = lastName
        self._phoneNumber = phoneNumber

    @property
    def get_firstname(self):
        return self._firstName


    @property
    def get_lastname(self):
        return self._lastName

    @property
    def get_phonenumber(self):
        return self._phoneNumber

    def set_firstname(self, firstName):
        self.__validatename(firstName)
        self._firstName = firstName

    def set_lastname(self, lastName):
        self.__validatename(lastName)
        self._lastName = lastName

    def set_phonenumber(self, phoneNumber):
        self.__validatephonenumber(phoneNumber)
        self._phoneNumber = phoneNumber



    def __validateinput(self, firstName, lastName, phoneNumber):
        self.__validatename(firstName)
        self.__validatename(lastName)
        self.__validatephonenumber(phoneNumber)


    def __validatename(self, name):
        if name.isspace():
            raise ValueError("Name cannot be an whitespace")
        if not name:
            raise ValueError("Name cannot be an empty string")
        if name.isdigit():
            raise ValueError("Name cannot be a number")

    def __validatephonenumber(self, phoneNumber):
        if phoneNumber.isalpha() :
            raise ValueError("Phone number must consist of digits only")
        if phoneNumber[0] == "+" and len(phoneNumber) < 8:
            raise ValueError("International numbers must require a minimum of 8 digits")
        if len(phoneNumber) < 4:
            raise ValueError("Numbers must require at least 4 digits")




