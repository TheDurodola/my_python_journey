import to_do_list_manager_functions

list_of_task = []
status_of_task = []

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
			add_task = input("Enter the task: ")
			list_of_task.append(to_do_list_manager_functions.add_to_list(add_task))
			status_of_task.append("[]")	

		case 2:
			to_do_list_manager_functions.view_all_tasks(status_of_task, list_of_task)

		case 3: 
			to_do_list_manager_functions.mark_task_as_completed(status_of_task, list_of_task)

		case 4:
			user_input = input("Enter the number of what you would like to delete: ")
			user_input = user_input-1
			to_do_list_manager_functions.delete_a_task(user_input, list_of_task)
			to_do_list_manager_functions.delete_status(user_input, status_of_task)
			
		case 5:
			menu_condition = 1
