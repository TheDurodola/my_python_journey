user_age = int(input("Enter age in YEARS: "))

heart_rate = 220 - user_age

print(f"Your current maximum heart rate is {heart_rate}bpm")

lower_percentile = heart_rate * 0.5
upper_percentile = heart_rate * 0.85

print(f"\nYour targeted heart rate should be between {lower_percentile}bpm - {upper_percentile}bpm")

