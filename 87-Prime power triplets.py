# https://projecteuler.net/problem=87

from itertools import compress

def eratosthenes_sieve(n):
	"""Finds all primes in range [1,n]."""
	numbers = [True for i in range(n + 1)]
	
	p = 2
	while (p**2 <= n):
		if numbers[p]:
			for i in range(p**2, n + 1, p):
				numbers[i] = False
		p += 1
		
	primes = compress(range(2, n + 1),numbers[2:])
	return list(primes)

primes = eratosthenes_sieve(10_000)

triplet = lambda x, y, z: pow(x, 2) + pow(y, 3) + pow(z, 4)

maximum = 50_000_000

total = set()
for p1 in primes:
	if triplet(p1, 0, 0) > maximum:
		break
	for p2 in primes:
		if triplet(p1, p2, 0) > maximum:
			break
		for p3 in primes:
			res = triplet(p1, p2, p3)
			if res < maximum:
				print(p1, p2, p3)
				total.add(res)
			else:
				break

print("\nTotal:", len(total))
