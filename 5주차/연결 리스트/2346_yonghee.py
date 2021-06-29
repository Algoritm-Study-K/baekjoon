N = int(input())
idx = 0
numbers = list(map(int, input().split()))
index = []
result = []

for i in range(1, N + 1):
	index.append(i)

while numbers:
	num = numbers.pop(idx)
	result.append(index.pop(idx))
	if not numbers:
		break
	if num < 0:
		idx = (idx + num) % len(numbers)
	else:
		idx = (idx + num - 1) % len(numbers)

for n in result:
	print(n, end = ' ')
print()