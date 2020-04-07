def solve(meal_cost, tip_percent, tax_percent):
    return print(round(meal_cost + ((meal_cost/100)*tip_percent) + ((meal_cost/100)*tax_percent)))