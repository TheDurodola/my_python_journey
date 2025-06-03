import bank_atm_functions

account_balance = [0]

menu_loop_condition = 0

while(menu_loop_condition<1):
	main_display = """
\t\tBANK ATM SIMULATION


1. DEPOSIT
2. WITHDRAW
3. TRANSACTIONS
0. EXIT
"""

	print(main_display)

	main_menu_input = int(input("Enter your choice: "))

	match(main_menu_input):
		case 1:
			print("\t\tDEPOSIT\n")
			deposit_amount = int(input("Enter the amount: ₦"))
			bank_atm_functions.deposit_amount(account_balance, deposit_amount)	
		case 2:
			withdraw_amount = int(input("Enter the amount (Max. ₦20,000 per transaction): ₦"))
			bank_atm_functions.withdraw_amount(account_balance, withdraw_amount)
		case 3:
			bank_atm_functions.view_transaction_logs() 
		case 0:
			menu_loop_condition = 1
		case _:
			print("\nINVALID OPTION")




