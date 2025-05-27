import to_do_list_manager_functions

list_of_task = []


menu_condition = 0
while menu_condition!=1:
	main_menu_display = """
\t\tTo-Do List Manager

1) Add a task
2) View tasks
3) Mark task as Completed
4) Delete task
5) Exit
"""
	print(main_menu_display)
	navigator = int(input("Enter your choice: "))
	match(navigator):
		case 1: 
			list_of_task.append(to_do_list_manager_functions.add_to_list())
		case 2:
			to_do_list_manager_functions.view_all_tasks(list_of_task)

		case 5:
			menu_condition = 1

print(list_of_task)


