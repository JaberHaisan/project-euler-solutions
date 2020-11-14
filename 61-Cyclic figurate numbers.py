triangle_number = lambda n: int(0.5 * n * (n + 1))
square_number = lambda n: n ** 2
pentagonal_number = lambda n: int(0.5 * n * (3 * n - 1))
hexagonal_number = lambda n: int(n * (2 * n - 1))
heptagonal_number = lambda n: int(n * (5 * n - 3) * 0.5)
octagonal_number = lambda n: int(n * (3 * n - 2))

# Convert numbers to string for easier splicing. Maximum n for each set of numbers was found manually by reversing operation 
# and finding value of n for 10,000.
triangle_numbers = [str(triangle_number(i)) for i in range(141 + 1) if 1000 <= triangle_number(i) < 10_000]
square_numbers = [str(square_number(i)) for i in range(100 + 1) if 1000 <= square_number(i) < 10_000]
pentagonal_numbers = [str(pentagonal_number(i)) for i in range(82 + 1) if 1000 <= pentagonal_number(i) < 10_000]
hexagonal_numbers = [str(hexagonal_number(i)) for i in range(71 + 1) if 1000 <= hexagonal_number(i) < 10_000]
heptagonal_numbers = [str(heptagonal_number(i)) for i in range(64 + 1) if 1000 <= heptagonal_number(i) < 10_000]
octagonal_numbers = [str(octagonal_number(i)) for i in range(58 + 1) if 1000 <= octagonal_number(i) < 10_000]

def prefix_dict(iterable, length=2):
	"""Generates a dict of prefixes for given iterable."""
	a_dict = {}
	for item in iterable:
		a_dict.setdefault(item[:length], []).append(item)
	return a_dict
				
def make_chain(num, a_list, length, chain=None):
	"""Tries to make a chain of numbers such that numbers form a circle according
	to the question's rules."""
	suffix = num[-2:]
	
	# Initializes chain during first iteration.
	if chain == None:
		chain = [num]
	
	# Check that required chain length is reached and that suffix of last number
	# is equal to prefix of initial number.	
	if len(chain) == length and chain[-1][-2:] == chain[0][:2]:
		print(chain, sum(int(num) for num in chain))
		return chain
		
	for num_type in a_list:
		prefixes = prefix_dict(num_type)
		if suffix in prefixes:
			for next_num in prefixes[suffix]:
				# Copies list and chain so that their modification does not affect the other nums to be checked.
				list_copy = a_list[:]
				list_copy.remove(num_type)
				chain_copy = chain[:]
				chain_copy.append(next_num)
				
				make_chain(next_num, list_copy, length, chain_copy)
	else:
		return None

num_types = [triangle_numbers, square_numbers, pentagonal_numbers, hexagonal_numbers, heptagonal_numbers]

# Start chain from octogonal numbers as they have the fewest members.
for octagonal_num in octagonal_numbers:	
	make_chain(octagonal_num, num_types, length=6)
