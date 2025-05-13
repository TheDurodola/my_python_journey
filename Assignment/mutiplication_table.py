
print("\t\t\t\tMULTIPLICATION TABLE")
print("\t\t\t\t====================\n")


for header in range(1,10):
	print("       ",header, end='')


print("\n===================================================================================")


for i in range(1,10):
	for x in range(1,10):
		print("", end='')
	print(i,end="||	 ")	
	for j in range(1,10):

		print(i*j, end=' \t    ')
	print("    ")

 