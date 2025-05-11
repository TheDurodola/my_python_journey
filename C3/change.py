print("Note: Client pays with a Dollar(1 Dollar= 100 cents)")
purchase_price = int(input('Enter the purchase price(in CENTS): '))


change = 100 - purchase_price

quarters = change//25
change= change%25

dimes = change//10
change = change%10

pennies = change


print(f"Your change is {quarters} quarters,{dimes} dimes, and {pennies} pennies")


