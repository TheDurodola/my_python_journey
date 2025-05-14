#Ex 3.8




first_number = int(input("Enter number 1: "))

smallest= first_number
largest= first_number
sum = first_number
product= first_number

for run in range(1,4):
	number = int(input(f"Enter number {run+1}: "))		
	sum = sum+number
	product = product*number
	average = sum/(run+1)
	if number>largest: 
		largest=number
	if number<smallest:
		smallest=number

print(f"\nThe Sum of the {run+1} integers is ", sum)
print(f"The Product of the {run+1} integers is ", product)
print(f"The Average of the {run+1} integers is ",average)
print(f"The Largest integer amongst the four is ",largest)
print(f"The Smallest integer amongst the four is ", smallest)


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