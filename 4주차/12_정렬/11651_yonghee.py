from sys import stdin

N = int(input())
numbers = []
for i in range(N):
	numbers.append(list(map(int, stdin.readline().split())))

numbers = sorted(numbers, key=lambda x: (x[1], x[0]))

for i in range(N):
	print(numbers[i][0], numbers[i][1])