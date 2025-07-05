first_number = int(input("Enter your first number: "))
second_number = int(input("Enter your second number: "))
third_number = int(input("Enter your third number: "))

smallest_number=0
middle_number=0
biggest_number=0


if first_number> second_number and first_number>third_number:
	biggest_number=first_number
if second_number> first_number and second_number>third_number:
	biggest_number=second_number
if third_number> second_number and third_number>first_number:
	biggest_number=third_number

if first_number< second_number and first_number<third_number:
	smallest_number=first_number
if second_number< first_number and second_number<third_number:
	smallest_number=second_number
if third_number< second_number and third_number<first_number:
	smallest_number=third_number

if first_number != biggest_number and first_number!=smallest_number:
	middle_number=first_number
if second_number != biggest_number and second_number!=smallest_number:
	middle_number=second_number
if third_number != biggest_number and third_number!=smallest_number:
	middle_number=third_number 



print(f"\nThe Number in Ascending Order is {smallest_number},{middle_number},{biggest_number}")