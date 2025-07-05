import bank_app_functions
from unittest import TestCase


class TestCube(TestCase):
	def test_that_create_account_function_exists(self):
		bank_app_functions.create_account()

		