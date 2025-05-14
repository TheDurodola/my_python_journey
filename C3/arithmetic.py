#Ex 3.8


sum=0
product=1
largest = 0
smallest = 0

for run in range(4):
	number = int(input(f"Enter the {run+1} number: "))
	
	first_number=number
	sum = sum+number
	product = product*number
	average = sum/(run+1)
	if number>largest: 
		largest=number
	if number<first_number:
		smallest=number

print(f"\nThe Sum of the {run+1} integers is ", sum)
print(f"The Product of the {run+1} integers is ", product)
print(f"The Average of the {run+1} integers is ",average)
print(largest)
print(smallest)



"""
if number_1 > number_2 and number_1>number_3 and :
	print("The First integer is the largest")

if number_2 > number_1 and number_2>number_3:
	print("2nd integer is the largest")

if number_3 > number_2 and number_3>number_1:
	print("3rd integer is the largest")




if number_1 < number_2 and number_1<number_3:
	print("The First integer is the smallest")

if number_2 < number_1 and number_2<number_3:
	print("2nd integer is the smallest")

if number_3 < number_2 and number_3<number_1:
	print("3rd integer is the smallest")"""