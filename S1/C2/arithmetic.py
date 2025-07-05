number_1 = int(input("Enter the First number: "))
number_2 = int(input("Enter the Second number: "))
number_3 = int(input("Enter the Third number: "))


sum = number_1 + number_2 + number_3
product = number_1 * number_2 * number_3


print("The Sum of the three integers is ", sum)
print("The Product of the three integers is ", product)

if number_1 > number_2 and number_1>number_3:
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
	print("3rd integer is the smallest")