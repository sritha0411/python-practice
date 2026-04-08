# Write your solution here
import math
def distance(x1,x2,y1,y2):
    d=math.sqrt((x2-x1)**2 + (y2-y1)**2)
    return d
x1=float(input())
y1=float(input())
x2=float(input())
y2=float(input())
a=distance(x1,x2,y1,y2)
print(round(a,2))