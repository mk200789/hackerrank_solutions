def split_number():
	n = input()
	l = []
	for i in xrange(n):
		h = raw_input()
		h = h.replace('-', ' ').split()
		l.append("CountryCode="+h[0]+",LocalAreaCode="+h[1]+',Number='+h[2])

	for i in l:
		print i


if __name__ == "__main__":
	split_number()