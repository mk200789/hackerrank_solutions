def extra_long_factorials():
	number = input()
	n = 1
	solution = 1

	while(n <= number):
		solution *= n
		n += 1

	return solution


if __name__ == '__main__':
	print extra_long_factorials()
