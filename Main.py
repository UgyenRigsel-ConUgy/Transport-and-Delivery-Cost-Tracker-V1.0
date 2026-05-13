#      Transport Cost Tracker V1.0

import calculation

#      Basic Transport Cost 
print("[Part 1: BASIC COST for TRANSPORT]") ")
distance = float(input("Distance to be traveled(km): "))
efficiency = float(input("Fuel efficiency of vehicle(km/L): "))

fuel_price = float(input("Price of fuel per liter: ")) 
profit_percentage = float(input("Desired profit percentage: "))

#        Data Input Validator
if distance <=0 or efficiency <=0 or fuel_price <=0:
    print("Please enter valid numbers for distance, efficiency, and fuel price.")
else:
#   Cost Tracker for Transport and Desired Profit
    fuel_used = calculation.fuel_consumption(distance, efficiency)
    cost = calculation.basic_cost(fuel_used, fuel_price)
    final_price = calculation.final_profit(cost, profit_percentage)


    print(f"Estimated fuel used is {fuel_used} Litres")

    print(f"Total estimated cost of fuel is {cost:.2f}")
    print(f"At a profit of {profit_percentage} the amount charged should be{final_price:.2f}")
