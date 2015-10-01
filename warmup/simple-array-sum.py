

size = input()
array1 = raw_input().split()
solution = 0

for x in xrange(size):
	solution += int(array1[x])

print solution