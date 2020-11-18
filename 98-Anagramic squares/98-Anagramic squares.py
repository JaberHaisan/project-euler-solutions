# https://projecteuler.net/problem=98

with open("98-anagrams.txt") as f_obj:
	words = f_obj.read().replace("\"", "").split(",")

letters_dict = {}
for word in words:
	letters = tuple(sorted(word))
	letters_dict.setdefault(letters, []).append(word)
	
anagrams = {}
lengths = set()
for k, v in letters_dict.items():
	if len(v) > 1:
		anagrams[k] = v
		lengths.add(len(k))

def digit_squares(n):
	"""Generates all squares with n digits and returns a list of strings."""
	squares = []
	b = 1
	while True:
		square = pow(b, 2)
		square_str = str(square)
		if len(square_str) == n:
			squares.append(square_str)
		if len(square_str) > n:
			break
		b += 1
	return squares 

# Create a dictionary of squares for all word lengths present in anagrams
# to minimize calls to digit_squares.	
squares = {i: digit_squares(i) for i in lengths}

# All squares that can be used to form a square anagram word pair.
all_angram_squares = []

for letters, anagrams in anagrams.items():
	length = len(letters)
	squares_set = set(squares[length])

	for square in squares[length]:
		anagram_squares = [int(square)]
		first = anagrams[0]
		
		# Making a map for translating anagrams.
		num_map = {}
		for i in range(length):
			ordinal = ord(first[i])
			square_digit = square[i]
			# Stop if letters don't have unique values.
			if square_digit in num_map.values():
				break
			num_map[ordinal] = square_digit
		# Only continue if letters have unique values.	
		else:
			for word in anagrams[1:]:
				new_num = word.translate(num_map)
				anagram_squares.append(int(new_num))
				if new_num not in squares_set or new_num.startswith("0"):
					break
			else:
				all_angram_squares.extend(anagram_squares)

print(max(all_angram_squares))
