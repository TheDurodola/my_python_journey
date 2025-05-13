import math

euler_number = 1

for repeating in range(1,11):
	divisor = 1/math.factorial(repeating)
	euler_number = euler_number+divisor

print(f'The value of e the {repeating}th summation is {euler_number}')
