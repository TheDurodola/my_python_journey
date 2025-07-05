number_of_students = int(input("Enter the number of students: "))

highest_score = 0
highest_name = 0
for classroom in range(number_of_students):
	student_name = input("\nEnter the student name: ")
	student_score = int(input("Enter the student score: ")) 
	if student_score>highest_score:
		highest_score = student_score
		highest_name = student_name

print(f'\nThe student with the highest of {highest_score} is {highest_name}')
