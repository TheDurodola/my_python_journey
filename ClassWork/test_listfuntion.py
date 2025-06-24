import unittest
import listfuntion


class TestListFunctions(unittest.TestCase):
    def test_get_length_works(self):
        actual = listfuntion.length([1, 2, 3])
        self.assertEqual(actual, 3)  # add assertion here


    def test_get_sum_of_items_at_even_index_works(self):
        actual = listfuntion.sum_of_items_at_even_index([1, 2, 3, 4, 5])
        self.assertEqual(actual, 9)

    def test_get_sum_of_items_at_odd_index_works(self):
        actual = listfuntion.sum_of_items_at_odd_index([1, 2, 3, 4, 5])
        self.assertEqual(actual, 6)

    def test_get_sum_of_items_at_every_third_position_works(self):
        expected = listfuntion.multiplication_of_items_at_every_third_position([1, 2, 3, 4, 5,6,])
        self.assertEqual(expected, 18)


    def test_get_average_works(self):
        actual = listfuntion.get_average([1, 2, 3])
        self.assertEqual(actual, 2)
