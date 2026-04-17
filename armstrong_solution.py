def is_armstrong(n):
    actual=n
    a=len(str(n))
    digit,sum = 0,0
    for i in range(a):
        digit = actual % 10
        actual = actual // 10
        sum += pow(digit,a)
    if sum == n:
        print(f"{n} is an Armstrong number.")
    else:
        print(f"{n} is not an Armstrong number.")
is_armstrong(int(input()))