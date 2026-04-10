def multiple_sum(n):
    result=0
    for i in range(1,n):
        if i % 3 == 0 or i % 5 == 0:
            result += i
        
    return result
print(multiple_sum(int(input())))
    