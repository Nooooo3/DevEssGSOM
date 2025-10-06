# Financial helper
wage = int(input("Pls, insert your salary: "))
exp = int(input("Pls, insert your monthly expenditures: "))
term = int(input("how long do you want to invest? (months): "))
save = wage - exp
rate = 0.08 #banks' rate for savings
savings = round(save * (((1 + rate / 12) ** term - 1) / (rate / 12)))
print(f"If you invest {save} every month, after {term} months you will get about {savings}. Pretty good, isn't it?")
print (f"Good luck, bedolaga")