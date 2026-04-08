# Write your solution here
def selling_price(profit_percentage,cost_price):
    sp = cost_price + (profit_percentage/100)*cost_price
    return sp
cost_price = float(input())
profit_percentage = float(input())
a = selling_price(profit_percentage,cost_price)
print(round(a,2))