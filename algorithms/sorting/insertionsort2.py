############################################
# Unsorted array						   #
#	s - the size of the array			   #
#	ar - the sorted array of integers	   #
# 										   #
############################################

def insertionSort(ar):
	s = len(ar)
	for i in xrange(s-1):
		if ar[i] >= ar[i+1]:
			temp = ar[i]
			ar[i] = ar[i+1]
			ar[i+1] = temp

		if ar[i] < ar[i-1]:
			#print "less"
			while (i >= 1):
				if ar[i] < ar[i-1]:
					temp = ar[i]
					ar[i] = ar[i-1]
					ar[i-1] = temp
				i = i -1
		
		print " ".join("%d" %(num) for num in ar)

		
			
if __name__ == '__main__':
	s = 6
	ar = [1, 4, 3, 5, 6, 2]
	#s = 4
	#ar = [1, 4, 3, 5]
	insertionSort(ar)