import random

from ClassWork.listfuntion import length, sum_of_items_at_even_index, sum_of_items_at_odd_index, \
    multiplication_of_items_at_every_third_position, get_average

list_of_numbers = []

for items in range(10):
    number = random.randint(1, 52)
    list_of_numbers.append(number)

print(length(list_of_numbers))
print(sum_of_items_at_even_index(list_of_numbers))
print(sum_of_items_at_odd_index(list_of_numbers))
print(multiplication_of_items_at_every_third_position(list_of_numbers))
print(get_average(list_of_numbers))