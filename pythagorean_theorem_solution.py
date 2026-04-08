# Write your solution here
import math
def pythagorean(a,b):
    c = math.sqrt(a**2 + b**2)
    return c
a=float(input())
b=float(input())
d=pythagorean(a,b)
print(round(d,2))