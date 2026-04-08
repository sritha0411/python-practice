# Write your solution here
def bmi_calculator(w,h):
    bmi=w/h**2
    return bmi
w=float(input())
h=float(input())
a=bmi_calculator(w,h)
print(round(a,2))