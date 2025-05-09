"""
PROMPT your user to enter an integer
Store the entered integer as total_spending

if the total_spending is greater than or equal to 1_000 and is lesser than or equal to 10_000
	MULTIPLY the total_spending by 0.05 (%5)
	STORE the result as discount and DISPLAY the discount to the user
	MINUS the discount from the total_spending and the DISPLAY the result to the user

elif the total_spending is greater than 10_000 and is lesser than or equal to 50_000
	MULTIPLY the total_spending by 0.1 (%10)
	STORE the result as discount and DISPLAY the discount to the user
	MINUS the discount from the total_spending and the DISPLAY the result to the user

elif the total_spending is greater than 50_000
	MULTIPLY the total_spending by 0.2 (%20)
	STORE the result as discount and DISPLAY the discount to the user
	MINUS the discount from the total_spending and the DISPLAY the result to the user
else
	PRINT "INVALID AMOUNT"

"""



total_spending = float(input("Enter the total spending: ₦"))

if total_spending>=1000 and total_spending<=10_000:
	discount = total_spending*0.05
	print(f"Your discount is ₦{discount:,.2f}")
	print(f"Your amount to be paid is ₦{total_spending-discount:,.2f}")

elif total_spending>10_000 and total_spending<=50_000:
	discount = total_spending*0.10
	print(f"Your discount is ₦{discount:,.2f}")
	print(f"Your amount is ₦{total_spending-discount:,.2f}")

elif total_spending>50_000:
	discount = total_spending*0.20
	print(f"Your discount is ₦{discount:,.2f}")
	print(f"Your amount is ₦{total_spending-discount:,.2f}")
else:
	print("INVALID AMOUNT. BROKIE")
	