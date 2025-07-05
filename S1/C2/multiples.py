number_1 = 1024
number_2 = 2

number_1a = number_1 %4
number_2a = number_2 % 10

if number_1a == 0:
	print("1024 is a multiple of 4")
else:
	print("It isn't")


if number_2a ==0:
	print("It is a multiple of 10")
else: 
	print("It isn't")