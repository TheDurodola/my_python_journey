import nokia_function

counter =1
while counter>0:

	loading_screen = """ 	
		NOKIA 3310

1) Turn-On
0) Turn-Off

"""
	print(loading_screen)
	navigate = int(input("Enter a number to move: "))
	if navigate==0:
		counter=0
	if navigate==1:
		nokia_function.main_menu()		











