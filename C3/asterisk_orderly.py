#Ex 3.18


for i in range(1, 11):
	print(f'{'*' * i:<10} {'*' * (11 - i):<10} {' ' * i + '*' * (11 - i)} {' ' * (10 - i) + '*' * i}')