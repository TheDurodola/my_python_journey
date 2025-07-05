first_number = 4
numerator = 4
denominator = 3
stopper = 0

for num in range(100000000):
	fraction = numerator/denominator
	if num%2!=0:
		fraction = fraction
	if num%2==0:
		fraction = -fraction

	first_number = first_number + (fraction)
	if round(first_number,2) == 3.14 and stopper<1:
			print(f"At the {num}th term, the number {first_number:.2f} is achieved")
			stopper = stopper +1
	if round(first_number,3) == 3.141 and stopper<2:
			print(f"At the {num}th term, the number {first_number:.3f}is achieved")
			stopper= stopper + 1
	if round(first_number,4) == 3.1415 and stopper<3:
			print(f"At the {num}th term, the number {first_number:.4f} is achieved")
			stopper = stopper +1
	if round(first_number,5) == 3.14159 and stopper<4:
			print(f"At the {num}th term, the number {first_number:.5f} is achieved", end="")
			stopper = stopper +1
			break

	denominator = denominator +2
	#print(f"{num+1}		||	{first_number:.5f}")