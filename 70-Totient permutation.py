# https://projecteuler.net/problem=70

from itertools import compress

def eratosthenes_sieve(n):
	"""Finds all primes in range [1,n]."""
	numbers = [True for i in range(n+1)]
	
	p = 2
	while (p**2 <= n):
		if numbers[p]:
			for i in range(p**2, n + 1, p):
				numbers[i] = False
		p += 1
		
	# Remove 0 and 1
	primes = compress(range(2, n+1), numbers[2:])
	return list(primes)

primes = eratosthenes_sieve(10_000_000)
primes_set = set(primes)

def prime_factors(num):
	"""Returns set of prime factors of num."""	
	factors = []
	for prime in primes:
		# Skip over the rest if already at last prime.
		if num in primes_set:
			factors.append(num)
			break
		if num == 1:
			break
		while num % prime == 0:
			factors.append(prime)
			num /= prime
			
	return set(factors)

def is_permutation(a, b):
	"""Returns True if b is a permutation of a."""
	a_str = str(a); b_str = str(b)
	
	if len(a_str) != len(b_str):
		return False
		
	for digit in set(a_str):
		if a_str.count(digit) != b_str.count(digit):
			return False
	else:
		return True

def phi(num):
	"""Returns total number of coprimes of num."""
	if num in primes_set:
		return num - 1
	phi_value = num
	for factor in prime_factors(num):
		phi_value *= 1 - (1 / factor)
	return int(phi_value)

n = 0	
min_ratio = float("inf")

for num in range(2, int(1e7)):
	print(num)
	phi_value = phi(num)
	if is_permutation(num, phi_value):
		ratio = num / phi_value
		if ratio < min_ratio:
			min_ratio = ratio
			n = num

print("\nMin ratio n:", n)
