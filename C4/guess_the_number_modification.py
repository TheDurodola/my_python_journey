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
				if user_input-computer_choice<=10 and user_input-computer_choice>=1:
					loop_counter = round(loop_counter/2)

				if abs(computer_choice-user_input)<=10 and abs(computer_choice-user_input)>=1:
					loop_counter = round(loop_counter/2)

			if loop_counter<10:
				print(f"{loop_counter} Tries. Either you know the secret or you got lucky!\n")
			if loop_counter>10:
				print(f"{loop_counter} Tries. You should be able to do better!\n")

			replay = input("Do you wish to continue (YES or NO)")
			if replay=="NO":
				loop_continuation=1
			if replay=="YES":
				loop_continuation=0	