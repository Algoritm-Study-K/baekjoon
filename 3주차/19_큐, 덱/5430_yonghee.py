from sys import stdin
T = int(input())

for _ in range(T):
	p = stdin.readline()
	n = int(stdin.readline())
	array = stdin.readline().strip('[]\n')

	if array == '':
		array = []
	else:
		array = list(map(int, array.split(',')))

	error = 0
	Rcount = 0
	for s in p:
		if s == "R":
			Rcount += 1
		elif s == "D":
			try:
				if Rcount % 2 == 0:
					array.pop(0)
				else:
					array.pop()
			except:
				error = 1
				break
	if error:
		print('error')
	else:
		if Rcount % 2 == 1:
			array = array[::-1]
		print(str(array).replace(', ', ','))