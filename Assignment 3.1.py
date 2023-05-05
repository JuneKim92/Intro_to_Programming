initial_investment = float(input("Please enter the initial investment as a whole number. For example an initial investment of $6000 would be entered as 6000: "))
print()
interest_rate = int(input("Please enter the interest rate as a whole number. For example if the rate is 6% then enter 6: "))
print()

year = 0 
new_investment = initial_investment

while new_investment < (initial_investment*2):
  new_investment = new_investment + ((interest_rate/100)*new_investment)
  year+=1

print("The number of years it takes for your investment to double is",year)
