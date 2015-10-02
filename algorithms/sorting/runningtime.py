############################################
# Modify insertionsort2.py keep track of   #
# the shifts made while sorting			   #
# 										   #
############################################

def insertionSort(ar):
	s = len(ar)
	print ar
	count = 0
	for i in xrange(s-1):
		if ar[i] > ar[i+1]:
			count += 1
			temp = ar[i]
			ar[i] = ar[i+1]
			ar[i+1] = temp

		if ar[i] < ar[i-1]:
			while (i >= 1):
				if ar[i] < ar[i-1]:
					count +=1
					temp = ar[i]
					ar[i] = ar[i-1]
					ar[i-1] = temp
				i = i -1
		
	print count

		
			
if __name__ == '__main__':
	s = 12
	#ar = [1, 1, 2, 2, 3, 5,5 , 7, 7, 9]
	#ar = [2,1,3,1,2]
	ar = [10, 9, 8, 7, 6, 5,4,3,2,1]
	insertionSort(ar)