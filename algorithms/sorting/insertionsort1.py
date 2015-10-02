############################################
# The premise that list is already sorted  #
#	s - the size of the array			   #
#	ar - the sorted array of integers	   #
############################################

def insertionSort(ar, s):
	#the unsorted number saved in temp
	found = False
	temp = ar[s-1]

	for i in reversed(xrange(1, s)):
		if temp <= ar[i]  and temp < ar[i-1]:
			ar[i] = ar[i-1]
		else:
			ar[i] = temp
			found = True
			break

		print " ".join("%d" %(num) for num in ar)

	if found:
		print " ".join("%d" %(num) for num in ar)
	else:
		ar[0] = temp
		print " ".join("%d" %(num) for num in ar)


		
			
if __name__ == '__main__':
	s = 10
	ar = [2, 3, 4, 5, 6, 7, 8, 9, 10, 1]
	insertionSort(ar, s)