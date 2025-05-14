#Ex 3.16




first_number = int(input("Enter number 1: "))

largest = first_number
second_largest = 0


for repeat in range(1,11):
	number= int(input("Enter number: "))
	if number>largest and number>second_largest: 
			largest = number
	if number>second_largest and number<largest:
			second_largest=number
	if largest==second_largest:
		second_largest=number
print(f"\nThe Largest integer is ",largest)
print(f"The Second integer is ",second_largest)

"""if student_score>highest_score and student_score>second_score:
		highest_score = student_score
		highest_name = student_name
	if student_score>second_score and student_score<highest_score:
		second_score = student_score
		second_name = student_name
"""