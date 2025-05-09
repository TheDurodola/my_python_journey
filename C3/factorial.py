number = int(input("Enter the number: "))
number_result = number
factorial = 1;
while number>0:
	factorial = factorial * number
	number = number-1
	
print(f"{number_result}! is {factorial}")

"""When doing above 1500(ValueError: Exceeds the limit (4300 digits) for integer string conversion; use sys.set_int_max_str_digits() to increase the limit)"""