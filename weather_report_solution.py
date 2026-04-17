def is_prime(x):
    if x<2:
        return False
    for i in range(2,x-1):
        if x%i==0:
            return False
    return True
    
def weather_report(n):
    for i in range(1,n+1):
        if is_prime(i):
            print("Clear Sky")
        elif i%4==0 and i%7==0:
            print("Thunderstorm")
        elif i%4==0:
            print("Sunny")
        elif i%7==0:
            print("Rainy")
        else:
            print(i)

weather_report(int(input()))