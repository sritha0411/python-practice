# Write your solution here
def volumeofcone(r,h):
    pi=3.14159
    volume=(1/3)*pi*r**2*h
    return volume
r=float(input())
h=float(input())
a=volumeofcone(r,h)
print(round(a,2))