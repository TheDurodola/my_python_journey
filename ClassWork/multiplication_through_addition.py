def multiply(number1,number2):


	number=0
	for index in range(number2):
		number = number + number1
	return number


number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

print(f"\nThe multiplication of {number1} and {number2} is",multiply(number1,number2))







