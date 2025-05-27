from bank_app_functions import bank_database, create_account, withdraw_amount, deposit_amount, retrieve_all_records, get_existing_account
from unittest import TestCase


class TestBankApp(TestCase):
	def test_that_create_account_function_exists(self):
		create_account(98823233534, "Bolaji", "08012345678")

	def test_that_withdrawal_exist(self):
		withdraw_amount(0,5566)

	def test_that_deposit_exist(self):
		deposit_amount(0,5566)

	def test_that_retrieve_all_records_exist(self):
		retrieve_all_records([])

	def test_that_get_existing_account_exist(self):
		get_existing_account([],6)
	
	def test_that_amount_deposit_reflects_on_the_balance(self):
		actual = deposit_amount(0,6000)
		expected = 6000
		self.assertEqual(actual, expected)
	
	def test_that_amount_withdrawn_reflects_on_the_balance(self):
		actual = withdraw_amount(500,500)
		expected = 0
		self.assertEqual(actual, expected)

	def test_that_the_create_function_can_create_multiple_accounts(self):
		create_account(98823233534, "Bolaji", "08012345678")
		create_account(98823232334, "ife", "080124345678")
		self.assertEqual(3,len(bank_database))
		#SeeingThePreviouslyAddedAccount

	def test_that_you_cant_withdraw_more_than_the_balance(self):
		actual = withdraw_amount(0,500)
		expected = 0
		self.assertEqual(actual,expected)
	
	def test_that_you_cant_withdraw_strings(self):
		actual = withdraw_amount(0,'DEMO')
		expected = 0
		self.assertEqual(actual, expected)

	def test_that_you_can_retrieve_all_accounts_in_the_database(self):
		retrieve_all_records(bank_database)

	def test_that_the_withdrawal_function_can_accept_real_numbers(self):
		actual = withdraw_amount(100,50.65)
		expected = 49.35
		self.assertEqual(actual, expected)

	def test_that_the_withdrawal_function_rejects_negative_figures(self):
		actual = withdraw_amount(100,-6)
		expected = (100)
		self.assertEqual(actual, expected)

	def test_that_a_particular_account_can_be_retrive_using_the_account_number(self):
		actual = get_existing_account(bank_database, 98823232334)
		expected = [98823232334, "ife", "080124345678"]
		self.assertEqual(actual, expected)
		

	
	


	

		