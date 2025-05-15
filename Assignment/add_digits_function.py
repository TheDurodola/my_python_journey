def add_digits(number):
	numbers=number
	sum = 0
	divisor=10_000

	if numbers<1 or numbers>10_000:
		sum = "INVALID INPUT!!!"

	else: 
		while divisor>0:
			collector = numbers//divisor
			numbers = number%divisor
			divisor = divisor//10
			sum = sum + collector

	return sum


digits = int(input("Enter your number: "))
print("The sum of every digits is", add_digits(digits))