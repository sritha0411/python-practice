def is_prime(n):
    while (n>1):
        for i in range(2, n-1):
            n%i==0
            return False
        return True
    return False
print(is_prime(int(input())))