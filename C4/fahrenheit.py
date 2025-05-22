def temp_table(c):	
		f =  (9 / 5) * c + 32
		return f
	

print("CELCIUS		FAHRENHEIT")
for temp_index in range(1,101):
	print(f"{temp_index}{temp_table(temp_index):>20.1f}")