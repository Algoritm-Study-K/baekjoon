N = int(input())
count = 0
result = 0

while count < N:
	num = result
	found = False
	while not found:
		num += 1
		numstr = str(num)
		for i in range(len(numstr) - 2):
			if numstr[i] == '6' and numstr[i + 1] == '6' and numstr[i + 2] == '6':
				found = True
	result = num
	count += 1
print(result)