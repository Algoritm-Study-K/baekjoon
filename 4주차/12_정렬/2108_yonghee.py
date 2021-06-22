from sys import stdin
from collections import Counter

N = int(input())
numbers = []
for _ in range(N):
	numbers.append(int(stdin.readline()))

print("%.f"%(sum(numbers) / N))

numbers.sort()
print(numbers[N // 2])

c = Counter(numbers).most_common()

if N > 1:
	if c[0][1] == c[1][1]:
		print(c[1][0])
	else:
		print(c[0][0])
else:
	print(numbers[0])

print(numbers[N - 1] - numbers[0])