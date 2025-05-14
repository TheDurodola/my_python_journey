#Ex 3.19

for a in range(1,20):
	for b in range(1, 20):
		for c in range(1, 20):
			if c**2 == (a**2) +(b**2):
				print(f" {c}^2  = {b}^2 + {a}^2")