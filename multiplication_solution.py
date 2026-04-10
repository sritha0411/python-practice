def multiples(n,m):
    for i in range(1,m+1):
        result = n*i
        print(f"{n} * {i} = {result}")  
        
multiples(int(input()), int(input()))