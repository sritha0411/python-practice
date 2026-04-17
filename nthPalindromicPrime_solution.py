def is_prime(x):
	if x==0 or x==1:
		return False
	for i in range(2, x-1):
		if x%i==0:
			return False
	return True

def is_palimdrome(x):
	s = str(x)
	return s == s[::-1]

def nthPalindromicPrime(n):
	guess = 2
	count = -1
	while True:
		if is_prime(guess) and is_palimdrome(guess):
			count += 1
			if count==n:
				return guess
		guess += 1

print(nthPalindromicPrime(int(input())))

