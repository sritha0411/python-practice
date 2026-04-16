def countdown(n):
    while n>0:
        if n%3==0 and n%5==0:
            print("FizzBuzz")
            n-=2
        elif n%3==0:
            print("Fizz")
            n -= 1
        elif n%5==0:
            print("Buzz")
            n -= 1
        else:
            print(n)
            n-=1
countdown(int(input()))