capital = int(input("Enter the Investment amount: ₦"))
number_of_years = int(input("Enter the number of Years: ")) 
interest_rate =int(input("Enter the interest rate: %"))

interest_rate = interest_rate/100
print("\nDuration		ROI\n")

for yearly_interest in range(number_of_years):
	profit = capital * interest_rate
	investment_amount = round(capital + profit,2)
	print(f"Year {yearly_interest+1}   		₦{investment_amount:,.2f}")
	capital = investment_amount 