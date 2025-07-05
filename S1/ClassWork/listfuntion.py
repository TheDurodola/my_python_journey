def length(listparameter):
    number_of_number = 0
    for item in listparameter:
        number_of_number += 1
    return number_of_number



def sum_of_items_at_even_index(listparameter):
    number_of_number = 0
    for item in listparameter:
        number_of_number += 1
    sum_of_items = 0
    for index in range( number_of_number):
        if index % 2 == 0:
            sum_of_items = sum_of_items + listparameter[index]
    return sum_of_items



def sum_of_items_at_odd_index(listparameter):
    number_of_number = 0
    for item in listparameter:
        number_of_number += 1

    sum_of_items = 0
    for index in range(number_of_number):
        if index % 2 != 0:
            sum_of_items += listparameter[index]
    return sum_of_items


def multiplication_of_items_at_every_third_position(list):
    length_of_list = length(list)
    result = 1

    for index in range(2,length_of_list, 3):
        result = result * list[index]
    return result





def get_average(list):
    number_of_number = 0
    for item in list:
        number_of_number += 1

    sum_of_items = 0
    for item in list:
        sum_of_items += item
    return sum_of_items / number_of_number