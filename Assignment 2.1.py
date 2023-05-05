#part1
print("Welcome to Fiber Optic Cable Shopping")

company = input("Enter your company's name: ")

feets = float(input("Enter the number of fiber optic feets to be installed: "))

cost = feets * 0.87

print("Company Name: " + company)
print("Total cost: " + str(cost))



#part2
print("Welcome to Fiber Optic Cable Shopping")

company = input("Enter your company's name: ")

feets = float(input("Enter the number of fiber optic feets to be installed: "))

total_cost= feets * 0.87

if feets >= 100 and feets < 250:
    total_cost = feets * .80
elif feets>=250 and feets<500:
    total_cost = feets* .70
elif feets>=500:
    total_cost = feets*.50

print("Company Name: " + company)
print("Total cost: " + str(total_cost))

