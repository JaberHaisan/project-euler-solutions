# https://projecteuler.net/problem=75

def gcd(a, b):
	"""Returns gcd of a and b."""
	while b != 0:
		a, b = b, a % b
	return a

maximum_perimeter = 1_500_000

perimeter_dict = {}

# This uses Euclid's formula for generating pythagorean triplets.
for m in range(1, maximum_perimeter // 2):
	print(m)
	for n in range(1, m):
		
		b = 2 * m * n
		if b > maximum_perimeter:
			break
			
		# To generate only primitive pythagorean triplets m and n have to be coprime
		# and either m should be even and n odd or vice versa.
		# Sum of an odd number and an even number is always odd. 
		if gcd(m, n) == 1 and (m + n) % 2 != 0:
			a = pow(m, 2) - pow(n, 2)
			c = pow(m, 2) + pow(n, 2)
			
			initial_total = a + b + c
			
			total = initial_total
			n = 1
			while total <= maximum_perimeter:
				perimeter_dict[total] = perimeter_dict.get(total, 0) + 1
				n += 1
				total = n * initial_total
	
match = 0
for k, v in perimeter_dict.items():
	if v == 1:
		match += 1
print("\nRequired Triplets:", match)
