print("Enter a number between 1-10,000\n")

number = int(input("Enter your number: "))

finalnum=number
sum = 0
divisor=10_000

if number>10_000 or number<1:
	print("INVALID INPUT!!!")

else: 
	while divisor>0:
		collector = number//divisor
		number = number%divisor
		divisor = divisor//10
		sum = sum + collector


print(f"The sum of every digits in {finalnum} is {sum}")
		

	