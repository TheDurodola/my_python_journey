import unittest

from phonebookapp.phonebook import Phonebook


class TestPhonebook(unittest.TestCase):

    def setUp(self):
        self.phonebook = Phonebook()

    def test_contact_can_be_added_to_phonebook(self):
        self.phonebook.add_contact('John', 'Doe', '1234567890')
        self.assertEqual(1, self.phonebook.database_size())  # add assertion here


if __name__ == '__main__':
    unittest.main()
