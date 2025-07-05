from listfunction import get_even_numbers

list_of_number = [10, 20, 30, 40, 50]
print(list_of_number[2])


list_of_colors = ['red', 'green', 'blue']
list_of_colors_size = len(list_of_colors)
list_of_colors.pop(list_of_colors_size-1)
print(list_of_colors)


list_of_colors.append('purple')
print(list_of_colors)


list_of_new_number = [1, 2, 3, 4, 5]
list_of_new_number.remove(3)
print(list_of_new_number)


list_of_name = ['Alice', 'Bob', 'Charlie']
list_of_count = []
for name in list_of_name:
    count_of_name = len(name)
    list_of_count.append(count_of_name)

print(list_of_count)


list_of_number = [4, 1, 3, 9, 2]
list_of_number.sort()
print(list_of_number)


print(get_even_numbers(list_of_number))

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)


a = ["lamb", "kit", "yam", "kings", "dogs", "man"]
b = []
for string in a:
    if len(string) > 3:
        b.append(string)

print(b)