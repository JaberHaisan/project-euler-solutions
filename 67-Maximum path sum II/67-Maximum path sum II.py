# https://projecteuler.net/problem=67

from collections import deque

with open("67-triangle.txt") as f_obj:
	data = f_obj.read().splitlines()

# Removing / appending data from the ends of a deque is more efficient compared
# to a list
numbers = deque()
for row in data:
	numbers.append([int(num) for num in row.split()])

# Compress all rows into one.
for row_num in reversed(range(len(numbers) - 1)):
	new_row = []
	for i, prev_num in enumerate(numbers[row_num]):
		# Add number from previous row to it's two adjacent numbers in the
		# next row and select whichever number is larger. Then add it
		# to the compressed row.
		maximum = max([prev_num + next_num for next_num in numbers[row_num + 1][i: i + 2]])
		new_row.append(maximum)
		
	if len(numbers) > 2:
		# Remove rows used to make compressed row and add the compressed
		# row to numbers.
		for n in range(2):
			numbers.pop()
		numbers.append(new_row)
	else:
		# If length of numbers is 2 then all rows compressed.
		res = new_row[0]

print(res)
