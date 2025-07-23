import unittest

from phonebookapp.phonebook import Phonebook


class TestPhonebook(unittest.TestCase):

    def setUp(self):
        self.phonebook = Phonebook()


    def test_database_size_is_initially_zero(self):
        self.assertEqual(self.phonebook.database_size(), 0)

    def test_contact_can_be_added_to_phonebook(self):
        self.phonebook.add_contact('John', 'Doe', '1234567890')
        self.assertEqual(1, self.phonebook.database_size())

    def test_add_contact_list_size_1_remove_one(self):
        self.phonebook.add_contact('John', 'Doe', '1234567890')
        self.assertEqual(1, self.phonebook.database_size())
        self.phonebook.delete_contact('John', 'Doe', '1234567890')
        self.assertEqual(0, self.phonebook.database_size())

    def test_add_contact_list_size_2_remove_one(self):
        self.phonebook.add_contact('John', 'Doe', '1234567890')
        self.phonebook.add_contact("Ade", "ire", "08148260470")
        self.phonebook.delete_contact("Ade", "ire", "08148260470")
        self.assertEqual(1, self.phonebook.database_size())

    def test_that_find_via_first_name_retrieves(self):
        self.phonebook.add_contact('John', 'Doe', '1234567890')
        self.assertEqual( ('John', 'Doe', '1234567890'), self.phonebook.find_contact_via_firstname('John'))

    def test_that_add_two_contacts_remove_one_assert_that_the_right_one_was_deleted(self):
        self.phonebook.add_contact('John', 'Doe', '1234567890')
        self.phonebook.add_contact("Ade", "ire", "08148260470")
        self.assertEqual(2, self.phonebook.database_size())
        self.phonebook.delete_contact("Ade", "ire", "08148260470")
        self.assertEqual(('John', 'Doe', '1234567890'), self.phonebook.find_contact_via_firstname('John'))
        self.assertIsNone(self.phonebook.find_contact_via_firstname('Ade'))

    def test_find_via_last_name_retrieves(self):
        self.phonebook.add_contact('John', 'Doe', '1234567890')
        self.assertEqual(('John', 'Doe', '1234567890'), self.phonebook.find_contact_via_lastname('Doe'))

    def test_that_add_two_contacts_remove_one_assert_that_find_via_lastname(self):
        self.phonebook.add_contact('John', 'Doe', '1234567890')
        self.phonebook.add_contact("Abolaji", "ire", "08148260470")
        self.assertEqual(2, self.phonebook.database_size())
        self.phonebook.delete_contact("Abolaji", "ire", "08148260470")
        self.assertEqual(('John', 'Doe', '1234567890'), self.phonebook.find_contact_via_firstname('John'))
        self.assertIsNone(self.phonebook.find_contact_via_firstname('Ade'))

    def test_find_contact_via_phonenumber(self):
        self.phonebook.add_contact('John', 'Doe', '1234567890')
        self.assertEqual(('John', 'Doe', '1234567890'), self.phonebook.find_contact_via_phonenumber('1234567890'))

    def test_that_add_two_contacts_remove_one_assert_that_using_find_with_phone_number(self):
        self.phonebook.add_contact('John', 'Doe', '1234567890')
        self.phonebook.add_contact("Abolaji", "ire", "08148260470")
        self.assertEqual(2, self.phonebook.database_size())
        self.phonebook.delete_contact("Abolaji", "ire", "08148260470")
        self.assertEqual(('John', 'Doe', '1234567890'), self.phonebook.find_contact_via_phonenumber('1234567890'))
        self.assertIsNone(self.phonebook.find_contact_via_firstname('Ade'))

    def test_that_contact_can_be_editted(self):
        self.phonebook.add_contact('John', 'Doe', '1234567890')
        self.phonebook.edit_contact("John","Ade", "ire", "08148260470")




if __name__ == '__main__':
    unittest.main()
