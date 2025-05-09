# password<8 = very weak
# password==8 = weak
#  8<password<16 = strong
# pasword>16 = very strong



password = input("Enter your password: ")

password_count = len(password)

if password_count < 8:
	print("\nPassword is very weak!")
if password_count == 8:
	print("\nPassword is weak!")
if password_count > 8 and password_count<=16:
	print("\nPassword is strong!")
if password_count > 16:
	print("\nPassword is very weak!")