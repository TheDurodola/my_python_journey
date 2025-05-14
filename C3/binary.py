binary = int(input("Enter your binary number: "))
initial_binary = binary
expo = len(str(binary))

decimal=1
picker= 10**(expo-1)

multiplier = 2**(expo-1)
while binary>0:
	operation = binary//picker
	binary = binary%picker
	picker = picker/10
	collector =operation* multiplier
	decimal=decimal + collector
	multiplier =multiplier/2

print(f"\nThe conversion of the BINARY number {initial_binary} is {decimal-1:.0f} in DECIMAL")