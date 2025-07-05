num = int(input("Enter your number: "))

numfinal = num
rev = 0

while num>0:
	rev = rev*10 + num%10
	num = num//10
	
if numfinal==rev:
	print("It is a palindrome number")
else:
	print("it is not a palindrome number")
	
