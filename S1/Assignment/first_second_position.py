number_of_students = int(input("Enter the number of students: "))

highest_score = 0
highest_name = 0
second_score = 0
second_name = 0


for classroom in range(number_of_students):
	student_name = input("\nEnter the student name: ")
	student_score = int(input("Enter the student score: ")) 
	if student_score>highest_score and student_score>second_score:
		highest_score = student_score
		highest_name = student_name
	if student_score>second_score and student_score<highest_score:
		second_score = student_score
		second_name = student_name

print(f'\nThe student with the highest of {highest_score} is {highest_name}')
print(f'The student with the second highest of {second_score} is {second_name}')
