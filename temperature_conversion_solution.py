# Write your solution here
def temparature(fahrenheit):
    celsius=(5/9)*(fahrenheit-32)
    return celsius
fahrenheit = float(input())
b=temparature(fahrenheit)
print(round(b,2))
