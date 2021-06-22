N = int(input())
numbers = []
for _ in range(N):
	numbers.append(int(input()))
for i in range(N - 1):
	for j in range(N - 1, i, -1):
		if numbers[j - 1] > numbers[j]:
			numbers[j - 1], numbers[j] = numbers[j], numbers[j - 1]

for i in range(N):
	print(numbers[i])

# 버블 정렬