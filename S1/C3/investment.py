principal = 1000
rate = 0.07
year = 1

print("YEAR	 ||	  AMOUNT")
print("============================")
for num in range(31):
	amount = (1+rate)**year
	amount = principal*amount
	print(f"{num+1}	 ||	${amount:,.2f}")
	year = year+1