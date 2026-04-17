n=int(input())
count=0
for i in range (1,n):
    temp = i
    while temp>0:
        if temp%10==7:
            count += 1
        temp //= 10
print(f"The number of 7's between 1 and {n} is {count}.")

