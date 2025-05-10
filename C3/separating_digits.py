"""
PROMPT the user to enter a five digits number and store as number
intialize divisor to 10000

	For each repeat
	false divide the num by divisor to store the rightmost digits
	with the use of module store the remaining values by number modulus divisor
	print the digit
	DIVIDE the divisor by 10 and repeat


"""



number = int(input("Enter the 5 digits number: "))
divisor = 10000
for repeat in range(5):
	digit = number//divisor
	number = number%divisor
	print(f'{digit}', end=' ')
	divisor = divisor//10