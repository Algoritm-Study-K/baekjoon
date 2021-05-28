C = int(input())
for _ in range(C):
	N = list(map(int, input().split()))
	sum = 0
	count = 0
	for i in range(1, len(N)):
		sum += N[i]
	avg = sum / N[0]
	for i in range(1, len(N)):
		if N[i] > avg:
			count += 1
	print("{0:0.3f}%".format(count / N[0] * 100))