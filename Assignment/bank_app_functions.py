import random


def get_existing_account(bank_database, wanted_account):
	for database in bank_database:
		if wanted_account == database[0]:
			return database
		if wanted_account!= database[0]:
			display =("INCORRECT ACCOUNT NUMBER")
			return print(display)




def get_submenu(bank_database):
		loop_condition = 0
		while loop_condition !=1:
			print(f"\n\t\t\tHi, {bank_database[1]}. What would you to do?")
			sub_menu_display = """
1) Deposit
2) Withdraw
3) Check Balance
4) Transfer
0) Exit
"""
			print(sub_menu_display)

			main_menu_user_input = int(input("Choose: "))

			match (main_menu_user_input):
				case 1:
					bank_database[3] = deposit_amount(bank_database[3])
				case 2: 
					bank_database[3] = withdraw_amount(bank_database[3])										
				case 3:
					print(f'Your account balance is currently ₦{bank_database[3]:,}')
				case 0:
					print("Thank you for using YRSD Bank")
					loop_condition = 1




def create_account():
	account_number = random.randint(1000000000,9999999999)
	account_details = [account_number]
	first_name = input("Enter first name: ")
	account_details.append(first_name)
	last_name = input("Enter last name: ")
	account_details.append(last_name)
	account_balance = 0
	account_details.append(account_balance)
	return account_details
	


def deposit_amount(balance):
	print("\nWELCOME TO THE DEPOSIT\n")
	amount_deposited = int(input("How much do you which to deposit: ₦"))
	balance = balance + amount_deposited
	print("\nProcessing.\nProcessing..\nProcessing...\n")
	print(f"₦{amount_deposited:,} has been deposited to your account")
	return balance 
	

def withdraw_amount(balance):
	print("\nWELCOME TO THE WITHDRAWAL\n")
	amount_withdrawn = int(input("How much would you like to withdraw: ₦"))
	balance = balance - amount_withdrawn
	print("\nProcessing.\nProcessing..\nProcessing...\n")
	print(f"₦{amount_withdrawn:,} has been withdrawn from your account")
	return balance 

	
	
		