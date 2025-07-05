import random

computer_1st_number = random.randint(1,9)
computer_2nd_number = random.randint(1,9)

print(f"How much is {computer_1st_number} times {computer_2nd_number}?")

loop_condition = 0

while loop_condition!=1:
	user_input = int(input("My choice is: "))
	if user_input==computer_1st_number*computer_2nd_number:
		print("Very Good!!!")
		loop_condition = 1
	else:
		print("No. Please try again.")