#########################################################
# n - the number of elements in the array ar			#
# the n elements of ar(including p at the begining)		#
# 										   				#
#########################################################


def partition(ar):
	p = ar[0]
	left = []
	right = []
	for i in xrange(1, len(ar)):
		if ar[i] < p:
			left.append(ar[i])
		else:
			right.append(ar[i])

	left.append(p)
	return " ".join(["%d" %i for i in (left + right)])

if __name__ == '__main__':
	#n = input()
	#ar = [int(i) for i in raw_input().split()]
	n = 5
	ar = [4, 5, 3, 7, 2]
	print partition(ar)