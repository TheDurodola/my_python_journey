import bank_atm_functions
from unittest import TestCase


class TestCube(TestCase):
	def test_that_deposit_amount_exist(self):
		account_balance = [0]
		bank_atm_functions.deposit_amount(account_balance, 50000)	
	
	def test_that_withdraw_amount_exist(self):
		account_balance = [0]
		bank_atm_functions.withdraw_amount(account_balance, 20000)

	def test_that_view_transaction_logs_exist(self):
		bank_atm_functions.view_transaction_logs() 

	def test_that_deposit_amount_work(self):
		account_balance = [0]
		actual = bank_atm_functions.deposit_amount(account_balance, 50000)
		expected = [50000]
		self.assertEqual(actual,expected)

	def test_that_withdraw_amount_work(self):
		account_balance = [50000]
		actual = bank_atm_functions.withdraw_amount(account_balance, 20000)
		expected = [29900]
		self.assertEqual(actual,expected)
	
	def test_that_deposit_amount_you_cant_deposit_a_negative_figure(self):
		account_balance = [0]
		actual = bank_atm_functions.deposit_amount(account_balance, -100000)
		expected = None
		self.assertEqual(actual,expected)
	
	
	def test_that_withdraw_amount_rejects_amount_that_are_not_multiple_of_500_or_1000(self):
		account_balance = [50000]
		actual = bank_atm_functions.withdraw_amount(account_balance, 1300)
		expected = None
		self.assertEqual(actual,expected)


	




