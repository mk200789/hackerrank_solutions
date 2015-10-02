def quickSort(ar):
	p = ar[0]
	left = []
	right = []
	for i in xrange(1, len(ar)):
		if ar[i] < p:
			left.append(ar[i])
		else:
			right.append(ar[i])

	left = sorted(left)
	right = sorted(right)
	left.append(p)
	#print " ".join(["%d" %i for i in (left + right)])
	return left + right

if __name__ == '__main__':
	n = 7
	ar = "5 8 1 3 7 9 2"
	ar = [int(i) for i in ar.split()]
	print quickSort(ar)