import bank_app_functions
import random

bank_database = []
main_menu_loop_condition=0
counter = 0




while main_menu_loop_condition!=1:

		main_menu_display = """
\t\t\tWELCOME TO YRSD BANK

1) Create Account
2) Existing Account
3) Menu
4) Print all existing accounts
0) Exit
"""
		print(main_menu_display)
		main_menu_input = int(input("What would you like to do: "))
		
		
		
		match(main_menu_input):
			
			case 1:
				bank_database.append(bank_app_functions.create_account())
				print(f"\nWelcome {bank_database[counter][1]}, your account number is {bank_database[counter][0]}\n")
				counter +=1
			
			case 2:
				existing_account_number = int(input("Enter your 10-Digits account number: "))
				current_account = bank_app_functions.get_existing_account(bank_database, existing_account_number)
				print(current_account)
				
			case 3:
				bank_app_functions.get_submenu(current_account)
			case 4:
				bank_app_functions.retrieve_all_records(bank_database)
				
			case 0:
				print("\nTHANK YOU FOR USING YRSD BANK")
				main_menu_loop_condition=1
		

		


			
	


