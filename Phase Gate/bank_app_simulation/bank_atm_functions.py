transaction_logs = []
charges = 100


def view_transaction_logs():
	if len(transaction_logs)>0:
		print("\t\tTRANSACTION LOGS\n Your transactions are as follows:")
		for index, log in enumerate(transaction_logs):
					print(f"{index+1} {log:,}")
	else:
		print("NO TRANSACTION AVAILABLE")


def deposit_amount(account_balance, deposit_amount):	
			if deposit_amount > 0:
				account_balance[0] = account_balance[0] + deposit_amount 
				print(f"\nYour current balance: ₦{account_balance[0]:,.2f}")
				transaction_logs.append((deposit_amount))
				return account_balance
				
			else:
				print("\nINVALID DEPOSIT AMOUNT")	

def withdraw_amount(account_balance, withdraw_amount):
			maximum_withdrawal_amount = account_balance[0] * 0.9
			if account_balance[0]>100:
				print("\t\tWITHDRAWAL\n")
				print("Note: Multiples of ₦500 or ₦1000")
				#withdraw_amount = int(input("Enter the amount (Max. ₦20,000 per transaction): ₦"))
				print(maximum_withdrawal_amount)
				if withdraw_amount <= maximum_withdrawal_amount and withdraw_amount<=20_000:
					if withdraw_amount%500==0 or withdraw_amount%1000==0: 
						account_balance[0] = account_balance[0] - withdraw_amount
						account_balance[0] = account_balance[0] - charges
						print(f"\nAMOUNT WITHDRAWN:{withdraw_amount:,.2f}\nWITHDRAWAL FEES {charges:.2f}") 
						print(f"\nYour current balance: ₦{account_balance[0]:,.2f}")
						transaction_logs.append(-(withdraw_amount))
						return account_balance
					else:
						print("INVALID AMOUNT!!!")
				else:
					print("\nINVALID WITHDRAW AMOUNT!!!")
			else:
				print("\nINSUFFICIENT FUNDS")
	

	



