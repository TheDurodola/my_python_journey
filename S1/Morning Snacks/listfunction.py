
def get_even_numbers(list_of_number):
    even_numbers = []
    for number in list_of_number:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers
