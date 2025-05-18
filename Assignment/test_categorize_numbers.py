import categorize_numbers
from unittest import TestCase

class TestCategorizeNumbers(TestCase):
	def test_that_fetch_categorized_numbers_exists(self):
		categorize_numbers.fetch_categorized_numbers(10,15,21,30,5)
	
	def test_that_fetch_categorized_correct_answer(self):
		actual = categorize_numbers.fetch_categorized_numbers(10,15,21,30)
		expected = "10 15 30" 
		self.assertEqual()