## Life expectancy
age = int(input("Pls, insert your age: "))
avg_age_rus = 74
avg_age_hk = 85
days_left = avg_age_rus * 365 - age * 365
days_diff = (avg_age_hk * 365) - (avg_age_rus * 365)
print(f"Average life expectancy in Russia is about {avg_age_rus}")
print(f"In average you still have to live for about {days_left} days more. Bruh...")
print(f"Average random man from Hong Kong will live {days_diff} days more.")