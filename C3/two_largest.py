#Ex 3.16


largest = 0
second_largest =0


for repeat in range(11):
	number= int(input("Enter the number"))
	if number>largest: 
			second_largest=largest
	#if second_largest>largest
			largest=number

print(largest)
print(second_largest)