count=int(input())
def decrementGlobal(a):
    a -= 2
    return a
print(decrementGlobal(count))
count=decrementGlobal(count)
print(count)