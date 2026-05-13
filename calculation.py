print("Enter the following details for calculating costs")

def fuel_consumption(distance,efficiency):
    fuel_used = distance / efficiency
    return fuel_used

def basic_cost(fuel_used, fuel_price):
    cost = fuel_used * fuel_price
    return cost

def final_profit(cost, profit_percentage):
    profit_amt = cost * (profit_percentage/100)
    final_pricing = cost + profit_amt
    return final_pricing