def simple_array_sum():
	size = input()
	array1 = raw_input().split()
	solution = 0

	for x in xrange(size):
		solution += int(array1[x])

	return solution


if __name__ == '__main__':
	print simple_array_sum()