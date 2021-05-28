alphabets = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
str = input()
sum = 0
for s in str:
	for i in range(len(alphabets)):
		if s in alphabets[i]:
			sum += i + 3
print(sum)