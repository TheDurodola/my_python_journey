import random

computer_1st_number = random.randint(1,9)
computer_2nd_number = random.randint(1,9)

print(f"How much is {computer_1st_number} times {computer_2nd_number}?")

loop_condition = 0

while loop_condition!=1:
	user_input = int(input("My choice is: "))
	if user_input==computer_1st_number*computer_2nd_number:
		loop_condition = 1
		postive_comment = random.randint(1,3)
		match postive_comment:
			case 1: print("Very good") 
			case 2: print("Nice work!") 
			case 3: print("Keep up the good work!'") 
		
			
	else:
		negative_comment = random.randint(1,3)
		match negative_comment:
			case 1: print("No. Please try again.") 
			case 2: print("No. Keep trying.") 
			case 3: print("'Wrong. Try once more.") 
