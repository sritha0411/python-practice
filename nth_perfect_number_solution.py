def is_perfect(n):
    if n < 2:
        return False
    divisor_sum = 0
    for i in range(1, (n//2)+1):
        if n%i==0:
            divisor_sum += i
    return divisor_sum==n
    
def nth_perfect(m):
    count=0
    current_num=1
    while count < m:
        if is_perfect(current_num):
            count += 1
            if count == m:
                return current_num
        current_num += 1
print(nth_perfect(int(input())))