def is_valid(a,b,c):
    if a + b > c and a + c > b and b + c > a:
        return True
    return False

def is_classified(a,b,c):
    if is_valid(a,b,c) and a==b==c:
        return "Equilateral"
    elif is_valid(a,b,c) and (a==b or b==c or c==a):
        return "Isosceles"
    elif is_valid(a,b,c) and a!=b!=c:
        return "Scalene"
    elif not is_valid(a,b,c):
        return "Invalid Triangle"
a,b,c=map(int,input().split())

print(is_classified(a,b,c))