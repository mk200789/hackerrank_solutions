def simple-array-sum():
	size = input()
	array1 = raw_input().split()
	solution = 0

	for x in xrange(size):
		solution += int(array1[x])

	return solution


if '__name__' == '__main__':
	simple-array-sum()