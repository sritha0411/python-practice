def harshad_number(n):
    actual = n
    sum = 0
    while n >0:
        remainder = n % 10
        n = n // 10
        sum = sum  + remainder
    # return sum
    if actual % sum == 0:
        return "True"
    
    return "False"

# def harshad_number(n):
#     if n % sum_of_digits==0:
#         print("True")
#     else:
#         print("False")

print(harshad_number(int(input())))