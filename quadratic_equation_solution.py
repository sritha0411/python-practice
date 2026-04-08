# Write your solution here
import math
def qudratic_euation(a,b,c):
    x = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)
    y = (-b - math.sqrt(b**2 - 4*a*c)) / (2*a)
    return x,y
a=float(input())
b=float(input())
c=float(input())
d,e=qudratic_euation(a,b,c)
print((d,e))