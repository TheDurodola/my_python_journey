bank_database = []

def create_account(account_number, name, phone):
	balance = 0
	account = [account_number, name, phone, balance]
	bank_database.append(account)
	return account
		

def deposit_amount(balance, amount_deposited):
	try:
		amount_deposited = float(amount_deposited)
		if amount_deposited <= 0:
			print("INVALID AMOUNT!!!. Enter a value greater than 0.")
			return balance
		else:
			balance = balance + amount_deposited
			return balance
	except ValueError:
		print("INVALID INPUT. AMOUNT SHOULD BE A NUMBER.")
		return balance



def withdraw_amount(balance, amount_withdrawn):
	try:
		amount_withdrawn = float(amount_withdrawn)
		if balance-amount_withdrawn<0:
			print("INSUFFICIENT FUNDS")
			return balance
		if amount_withdrawn <= 0:
			print("INVALID AMOUNT!!!. Enter a value greater than 0.")
			return balance
		else: 
			balance = balance - amount_withdrawn
			return balance
	except ValueError:
		print("INVALID INPUT. AMOUNT SHOULD BE A NUMBER.")
		return balance


def retrieve_all_records(bank_database):
	for index, records in enumerate(bank_database):
		print(index, records)


def get_existing_account(bank_database, wanted_account):
	for database in bank_database:
		if wanted_account == database[0]:
			return database
	
	
	
	
		