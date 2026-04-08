# Write your solution here
def compoundinterest(P,r,n,t):
    A = P * (1+r/n)**(n*t)
    return A
P = float(input())
r = float(input())/100
n = int(input())
t = float(input())
a=compoundinterest(P,r,n,t)
print(round(a,2))