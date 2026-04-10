def is_tidy(x):
    s = str(x)
    for i in range(len(s) - 1):
        if s[i] > s[i+1]: 
            return False
    return True
def nthTidyNumber(n):
    count = -1
    guess = 1
    while True:
        if is_tidy(guess):
            count += 1
            if count == n:
                return guess
        guess += 1
print(nthTidyNumber(int(input())))