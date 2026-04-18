def is_tidy(n):
    while n>0:
        remainder = n % 10
        n = n // 10
        temp = n % 10
        if remainder >= temp:
            pass
        else:
            return "Not Tidy"
    return "Tidy"
print(is_tidy(int(input())))