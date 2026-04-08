counter=int(input())
def incrementGlobal(a):
    a += 1
    return a
print(incrementGlobal(counter))
counter=incrementGlobal(counter)
print(counter)