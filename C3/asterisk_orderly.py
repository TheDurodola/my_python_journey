#Ex 3.18


NUMBER_OF_ASTERISK = 11

for loop in range(1,NUMBER_OF_ASTERISK):
	for looping in range(loop):
		print('*', end='')
	#print(" ")
	for looping in range(loop,NUMBER_OF_ASTERISK):
		print(' ', end='')
	for loop in range(11,9,-1):
		for looping in range(loop):
			print('*',end='')
	print(" ")


	
	