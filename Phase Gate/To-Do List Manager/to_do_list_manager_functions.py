def add_to_list():
	add_task = input("Enter the task: ")
	print("Task added!")
	return add_task

def view_all_tasks(list_of_task):
	for index, task in enumerate(list_of_task):
			print(index+1, task)
