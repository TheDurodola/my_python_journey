import random
difficulty_display = """
		DIFFICULTY SETTINGS
1) Easy
2) Hard
"""
print(difficulty_display)


user_difficulty = int(input("Enter your difficulty settings: "))

match user_difficulty:
	case 1:
		computer_1st_number = random.randint(1,9) 
		computer_2nd_number = random.randint(1,9)

	case 2:
		computer_1st_number = random.randint(1,99)
		computer_2nd_number = random.randint(1,99)

type_of_problem_display = """
1) Addition
2) Subtraction
3) Multiplication
4) Division
5) RANDOM

"""
print(type_of_problem_display)
type_of_problem = int(input("Enter a type of arithmetic problem you wish to solve: "))


match type_of_problem:
	case 1:	
		print("ADDITION HAS BEEN RANDOMLY CHOSEN!!!\n")
		print(f"How much is {computer_1st_number} plus {computer_2nd_number}?")

		loop_condition = 0

		while loop_condition!=1:
			user_input = int(input("My choice is: "))
			if user_input==computer_1st_number+computer_2nd_number:
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

	case 2:
		print("SUBTRACTION HAS BEEN RANDOMLY CHOSEN!!!\n")
		print(f"How much is {computer_1st_number} minus {computer_2nd_number}?")

		loop_condition = 0

		while loop_condition!=1:
			user_input = int(input("My choice is: "))
			if user_input==computer_1st_number-computer_2nd_number:
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

	case 3:
		print("MULTIPLICATION HAS BEEN RANDOMLY CHOSEN!!!\n")
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

	case 4:
		print("DIVISION HAS BEEN RANDOMLY CHOSEN!!!\n")
		print(f"How much is {computer_1st_number} divided {computer_2nd_number}?")

		loop_condition = 0

		while loop_condition!=1:
			user_input = int(input("My choice is: "))
			if user_input==computer_1st_number/computer_2nd_number:
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
	case 5:
		arithemetic_problem_random = random.randint(1,5)

		match arithemetic_problem_random:
			case 1:
				print(f"How much is {computer_1st_number} plus {computer_2nd_number}?")

				loop_condition = 0

				while loop_condition!=1:
					user_input = int(input("My choice is: "))
					if user_input==computer_1st_number+computer_2nd_number:
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

			case 2:
				print(f"How much is {computer_1st_number} minus {computer_2nd_number}?")
		
				loop_condition = 0

				while loop_condition!=1:
					user_input = int(input("My choice is: "))
					if user_input==computer_1st_number-computer_2nd_number:
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

			case 3:
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

			case 4:
				print(f"How much is {computer_1st_number} divided {computer_2nd_number}?")

				loop_condition = 0

				while loop_condition!=1:
					user_input = int(input("My choice is: "))
					if user_input==computer_1st_number/computer_2nd_number:
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

 

 



