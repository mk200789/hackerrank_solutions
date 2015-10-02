def time_in_word(h, m):
	t = {00: "o' clock", 01: "minute past", 02: "minutes past", 15: "quarter past" ,30: "half past", 31: "minutes to", 45: "quarter to"}
	num = {0: '', 1: 'one', 2: 'two', 3:'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11:'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen'}
	num1 = {1: 'teen', 2: 'twenty'}
	

	if m == 00:
		result = num[h]+ " "+ t[m] 
	elif m == 30:
		result = t[m] + " " + num[h]
	elif m  == 45 :
		result = t[m] + " " + num[h+1]
	elif m == 15:
		result = t[m] + " " + num[h]
	elif m > 00 and m < 15:
		if m == 01:
			result = num[1] + " " + t[01] + " "+num[h]
		else:
			result = num[m] + " " + t[02] + " " +num[h]
	elif m > 45 and m <=59:
		minute = 60 - m
		result = num[minute] + " " + t[31] + " " + num[h+1]
	elif m > 15 and m < 20:
		result = num[int(str(m)[1])] + " " + num1[int(str(m)[0])] + " " + t[02] + " " +num[h]
	elif m >= 20 and m <30:
		result = num1[int(str(m)[0])] + " " + num[int(str(m)[1])] + " " + t[02] + " "+num[h]
	elif m > 30 and m < 45:
		minute = 60 - m
		result = num1[int(str(minute)[0])] + " " + num[int(str(minute)[1])] + " " + t[31] + " "+num[h+1]

	return result

if '__main__' == __name__:
	h = 4
	m = 15
	print time_in_word(h,m)