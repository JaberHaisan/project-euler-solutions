# https://projecteuler.net/problem=95

from itertools import compress
from math import floor, sqrt

def eratosthenes_sieve(n):
	"""Finds all primes in range [1,n]."""
	numbers = [True for i in range(n+1)]
	
	p = 2
	while (p**2 <= n):
		if numbers[p]:
			for i in range(p**2, n + 1, p):
				numbers[i] = False
		p += 1
		
	primes = compress(range(2,n+1),numbers[2:])
	return primes

primes_set = set(eratosthenes_sieve(1_000_000))

def factors_sum(n):
	"""Returns sum of all proper factors of n."""
	factors = [1]
	if n not in primes_set:
		for i in range(2, floor(sqrt(n) + 1)):
			if n % i == 0:
				factors.append(i)
				multiple = n // i
				if multiple not in factors:
					factors.append(multiple)
	return sum(factors)

# Memoizing factors_sum.
sum_dict = {}

longest_chain = set()
longest_chain_length = 0

for i in range(2, 1_000_000):
	print(i)
	sum_set = set()
	n = i
	while True:
		# dict.setdefault always evaluates alternate result if called (which 
		# slows down the program significantly) even if it's not needed hence it is kept in the else loop 
		# so it only gets called in the case that n doesn't exist in dict to both set the value and
		# get the evaluated result at the same time.
		if n in sum_dict:
			n = sum_dict[n]
		else:
			n = sum_dict.setdefault(n, factors_sum(n))
		
		# Break loop if chain is not amicable or a member exceeds one million.	
		if n in sum_set or n > 1_000_000:
			break
			
		if n == i and len(sum_set) > 0:
			sum_set.add(i)
			if len(sum_set) > longest_chain_length:
				longest_chain_length = len(sum_set)
				longest_chain = sum_set
			break
			
		sum_set.add(n)

print("\nMin:", min(longest_chain))
