def is_prime(x):
	if x<2:
		return False
	for i in range(2, x):
		if x%i==0:
			return False
		return True

def is_tenly(x):
	digit_sum=sum(int(digit) for digit in str(x))
	return digit_sum == 10

def nthTenlyPrime(n):
	guess = 2
	count = -1

	while True:
		if is_tenly(guess) and is_prime(guess):
			count += 1
			if count == n:
				return guess
		guess +=1

print(nthTenlyPrime(int(input())))