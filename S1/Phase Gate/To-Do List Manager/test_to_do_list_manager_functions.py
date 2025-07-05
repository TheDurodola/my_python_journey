import to_do_list_manager_functions
from unittest import TestCase

list_of_task = ['OPO','AKAMU']
status_of_task = ["[]","[]"]

class TestCube(TestCase):
	def test_that_get_add_to_list_exist(self):
		to_do_list_manager_functions.add_to_list("POP")

	def test_that_get_view_all_tasks_exists(self):
		to_do_list_manager_functions.view_all_tasks(status_of_task, list_of_task)


	def test_that_add_to_list_works(self):
		actual = to_do_list_manager_functions.add_to_list("POP")
		expected = "POP"
		self.assertEqual(actual,expected)

	def test_that_view_all_task_works(self):
		actual = to_do_list_manager_functions.mark_task_as_completed(status_of_task, list_of_task)
		expected = ['[X]']
		self.assertEqual(actual,expected)

	def test_that_add_to_list_can_take_incase_the_brand_name_of_a_product_is_numerical(self):
		actual = to_do_list_manager_functions.add_to_list("33")
		expected = "33"
		self.assertEqual(actual,expected)

	def test_that_delete_status_works(self):
		actual = to_do_list_manager_functions.delete_status(0, status_of_task)
		expected =  ['[]'] 
		self.assertEqual(actual,expected)

	def test_that_delete_task_works(self):
		actual = to_do_list_manager_functions.delete_a_task(0, list_of_task)
		expected =  ['AKAMU']
		self.assertEqual(actual,expected)

				


	

		


