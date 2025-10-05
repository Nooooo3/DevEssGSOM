# Life on other planets
age = int(input("Enter your age: "))
pl1, pl2, pl3 = "Mercury", "Venus", "Mars"
age_mercury = age / 88 * 365
age_venus = age / 225 * 365
age_mars = age / 687 * 365
print(f"On {pl1} you would be {round(age_mercury)} y.o.")
print(f"On {pl2} you would be {round(age_venus)} y.o.")
print(f"On {pl3} you would be {round(age_mars)} y.o.")
print("Let's go live on Mars")