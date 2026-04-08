def outer(x):
    y=x/2
    m=inner(y)
    return m

def inner(x):
    y=x+1
    return y

x=int(input())
result=outer(x)
print(result)
