import unittest

from phonebookapp.contact import Contact


class TestContact(unittest.TestCase):

    def test_thatContactFirstNameCantBeAnEmptyString(self):
        contact = Contact('John', 'Doe', '1234567890')
        with self.assertRaises(ValueError):
            contact.set_firstname('')

    def test_thatContactLastNameCanBeAnEmptyString(self):
        contact = Contact('John', 'Doe', '1234567890')
        with self.assertRaises(ValueError):
            contact.set_lastname('')

    def test_thatContactFirstNameCantBeOnlyWhitespace(self):
        contact = Contact('John', 'Doe', '1234567890')
        with self.assertRaises(ValueError):
            contact.set_firstname('   ')

    def test_thatContactLastNameCantBeOnlyWhitespace(self):
        contact = Contact('John', 'Doe', '1234567890')
        with self.assertRaises(ValueError):
            contact.set_lastname('   ')

    def test_ThatContactFirstNameCantConsistOfNumbersOnly(self):
        contact = Contact('John', 'Doe', '1234567890')
        with self.assertRaises(ValueError):
            contact.set_firstname('12345')

        with self.assertRaises(ValueError):
            Contact('1', 'Durodola', '08148260470')

    def test_ThatContactLastNameCantConsistOfNumbersOnly(self):
        contact = Contact('John', 'Doe', '1234567890')
        with self.assertRaises(ValueError):
            contact.set_lastname('12345')

        with self.assertRaises(ValueError):
            Contact('John', '1', '08148260470')

    def test_thatContactPhoneNumberCantConsistOfLetters(self):
        contact = Contact('John', 'Doe', '1234567890')
        with self.assertRaises(ValueError):
            contact.set_phonenumber('abcde')

        with self.assertRaises(ValueError):
            Contact('John', 'Doe', 'abcde')

    def test_thatIfContactPhoneNumberIsAnInternationalNumberLengthMustBeMinimumOf8Digits(self):

        contact =    Contact('John', 'Doe', '+2348148260470')
        with self.assertRaises(ValueError):
            contact.set_phonenumber('+234')

    def test_localNumbersMustConsistOfAtLeast3Digits(self):
        contact = Contact('John', 'Doe', '1234567890')
        with self.assertRaises(ValueError):
            contact.set_phonenumber('00')











if __name__ == '__main__':
    unittest.main()
