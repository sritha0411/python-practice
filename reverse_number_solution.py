def reverse_num(n):
    temp = 0
    while n > 0:
        m = n % 10
        temp = (temp * 10) + m
        n = n // 10
    return temp
print(reverse_num(int(input())))