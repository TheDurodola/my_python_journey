import random
print("\t\t\t~WELCOME TO THE GUESS THE NUMBER GAME~")
print("\nGuess my number between 1 and 1000 with the fewest guesses\n")

loop_continuation = 0

while loop_continuation!=1:
			counter = 0
			computer_choice = random.randint(1, 1000)
			loop_counter = 0
			print(computer_choice)
			while counter!=1:
				user_input = int(input("Enter your guess: "))
	
				if user_input==computer_choice:
					print("Congratulations. You guessed the number!")
					counter=1

				if user_input<computer_choice:
					print("Too low. Try again.")
					loop_counter+=1

				if user_input>computer_choice:
					print("Too high. Try again.")
					loop_counter+=1

			print(f"\nYou have {loop_counter} failed tries before you got the correct answer.")
			replay = input("Do you wish to continue (YES or NO)")
			if replay=="NO":
				loop_continuation=1
			if replay=="YES":
				loop_continuation=0	