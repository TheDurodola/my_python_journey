"""
PROMPT your user to enter an amount to be invested
STORE the entered integer as capital

PROMPT your user to enter an the duration in years
STORE the entered integer as number_of_years

PROMPT your user to enter the interest rate in percentage
STORE the entered integer as interest_rate


DIVIDE the interest_rate by 100
STORE the entered integer as interest_rate

START a loop that increasing by 1 every LOOP and stops once its gets to the number_of_years
	MULTIPLY the capital by interest_rate
	STORE the result as profit
	
	ADD the profit and the capital
	STORE the result as investment amount
	PRINT the investment amount
	SAVE the investment_amount as the capital 


"""
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