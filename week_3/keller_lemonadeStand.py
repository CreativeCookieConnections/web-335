"""
Author: Aisha Keller
Date: 31 January 2026
File Name: keller_lemonadeStand.py
Description: Python program that simulates a lemonade stand with the cost of making lemonade and the profit from selling it.
"""

# Defining a function to calculate cost
def calculate_cost(lemons_cost, sugar_cost):  # Cost to make one cup of lemonade.
    return lemons_cost + sugar_cost

# Defining a function to calculate profit
def calculate_profit(lemons_cost, sugar_cost, selling_price):
    return selling_price - calculate_cost(lemons_cost, sugar_cost)

# Variables to test each function
lemons_cost = 0.50  # Cost of lemons per cup
sugar_cost = 0.20   # Cost of sugar per cup
selling_price = 1.50  # Selling price per cup

# variables to test each function
cost_per_cup =calculate_cost(lemons_cost, sugar_cost)
profit_per_cup =calculate_profit(lemons_cost, sugar_cost, selling_price)

# Call each function passing in variables
output = "Cost to make one cup of lemonade: ${0:.2f}\nProfit from selling one cup of lemonade: ${1:.2f}".format(cost_per_cup, profit_per_cup)

print(output)