def multiply(number1,number2):


	number=0
	if number2<0:
		number2 = - (number2)
		for index in range(number2):
			number = number + number1
	
	if number2>0:
		return number
	if number2<0:
		return number


number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

print(f"\nThe multiplication of {number1} and {number2} is",multiply(number1,number2))







