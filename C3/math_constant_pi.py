first_number = 4
numerator = 4
denominator = 3
for num in range(10000):
	fraction = numerator/denominator
	if num%2!=0:
		fraction = -fraction
	if num%2==0:
		fraction = fraction

	first_number = first_number -(fraction)
	if first_number == 3.14000:
			print(num)
	denominator = denominator +2
	print(f"{num+1}		||	{first_number:.5f}")