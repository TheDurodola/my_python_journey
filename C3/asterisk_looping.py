#Ex 3.17

for loop in range(11):
	for looping in range(loop):
		print('*', end='')
	print(" ")
print()
for loop in range(11,0,-1):
	for looping in range(loop):
		print('*',end='')
	print(" ")
	
print()

for loop in range(11):
	for looping in range(loop+1):
		print(' ', end='')
	
	for loop in range(loop,11):
		print('*', end='')
	print('')


print()


for loop in range(11):
	for looping in range(loop,11):
		print('', end=' ')
	
	for loop in range(loop+1):
		print('*', end='')
	print('')
