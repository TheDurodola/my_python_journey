import random
import time
#Time.time
print("\t\tSIMPLE ARITHMETIC APP")

start_time = time.time()

outer_loop_condition = 0
score = 0

while(outer_loop_condition<10):
	number1 = random.randint(1,1000)
	number2 = random.randint(1,1000)

	minuend = 0
	subratend = 0

	if number1 > number2: 
		minuend = number1
		subratend = number2

	if number2 > number1:
		minuend = number2
		subratend = number1
	
	tries = 0
	while(tries<2):
		result = minuend - subratend

		print(f"{minuend} - {subratend} ")

		user_input = int(input("= "))

		if user_input == result:
			print("BOOM!!! You got it right.")
			tries = 2
			score += 1

		if user_input != result:
			print("INCORRECT!!! Try again.")
			tries += 1
	outer_loop_condition = outer_loop_condition + 1

print(f"\nYour total score is: {score}")
end_time = time.time() - start_time
end_time = round(end_time)
print("Time taken is:",end_time,"seconds")




