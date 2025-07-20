import unittest

from sweetInTheMiddle import alpha


class Test(unittest.TestCase):

    def test_ifTheWordCantBeDividedAReminder(self):
        actual = alpha("joy", "ce")
        expected = "joyce"
        self.assertEqual(actual, expected)

        actual = alpha("ade", "ce")
        expected = "adece"
        self.assertEqual(actual, expected)


    def test_ifTheWordCanBeDividedWithoutAReminder(self):
        actual = alpha("love", "ce")
        expected = "loceve"
        self.assertEqual(actual, expected)

        actual = alpha("helloo", "ce")
        expected = "helceloo"
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
