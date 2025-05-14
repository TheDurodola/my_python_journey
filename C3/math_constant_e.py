euler_number = 1
denominator =1

for repeating in range(2,11):
	divisor = 1/denominator
	euler_number = euler_number+divisor
	denominator = denominator * repeating
print(f'The value of e the {repeating}th summation is {euler_number}')
