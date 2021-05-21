N = int(input())

def solve(x):
	count = 0
	for i in range(1, N + 1):
		if i <= 99:
			count += 1
			continue
		if i // 100 - i % 100 // 10 == i % 100 // 10 - i % 10:
			count += 1
	return count

print(solve(N))