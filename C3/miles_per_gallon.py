total=0
stop_program = 1
loop_count=0;
while stop_program != -1:
	gallons_used = float(input("Enter the gallons used: "))
	miles_driven = float(input("Enter the miles driven: "))
	miles_gallons = miles_driven/gallons_used
	print(miles_gallons)
	stop_program = int(input("Enter to -1 stop the program: "))
	loop_count=loop_count+1
	total=total+miles_gallons


total = total/loop_count
print(f"The overall average miles/gallon is {total}")