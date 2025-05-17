import nokia_function

counter =1
while counter>0:

	loading_screen = """ 	
╔════════════════════════════════════╗
║🔋 87%      🏠 HOME SCREEN   📶 LTE ║
╠════════════════════════════════════╣
║      				     ║
║        🕒 12:47 PM		     ║
║           			     ║
║          			     ║
╠════════════════════════════════════╣
║ 1) Main Menu        0) Switch-Off  ║
╚════════════════════════════════════╝
"""
	print(loading_screen)
	navigate = int(input("Enter a number to move: "))
	if navigate==0:
		counter=0
	if navigate==1:
		nokia_function.main_menu()		











