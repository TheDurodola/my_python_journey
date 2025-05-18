def fetch_categorized_numbers(*numbers, divisible_by = 5):
	end_of_loop = len(numbers)
	count_check = 0
	for index in range(0,end_of_loop):
		if numbers[index]%divisible_by==0: print(numbers[index], end=" ")






user_input =  input("Enter numbers separated by space: ")
numbers = [int(num) for num in user_input.split()]
divisible_by = int(input("Enter a divisor: "))
fetch_categorized_numbers(*numbers,divisible_by)	
		 