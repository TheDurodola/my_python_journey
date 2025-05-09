principal = 1000
rate = 0.07

year = 1
for num in range(31):
	amount = (1+rate)**year
	amount = principal*amount
	print(f"${amount}")
	year = year+1