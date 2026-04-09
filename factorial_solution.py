def is_factorial(n):
    if n==0 or n==1:
        return 1
    return n*is_factorial(n-1)

print(is_factorial(int(input())))