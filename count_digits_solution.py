import math
def digit_count(n):
    if n==0:
        return 1
    
    return math.floor(math.log10(abs(n)))+1

print(digit_count(int(input())))