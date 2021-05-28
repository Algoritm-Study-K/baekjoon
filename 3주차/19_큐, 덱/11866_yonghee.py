N, K = map(int, (input().split()))
queue = []
result = [None] * N

for i in range(1, N + 1):
	queue.append(i)

pointer = 0

for i in range(N):
	pointer += K - 1
	while pointer >= N:
		pointer -= N
	result[i] = queue.pop(pointer)
	N -= 1
print('<', end = '')
for s in result:
	if s == result[-1]:
		print(s, end = '')
	else:
		print("{0}, ".format(s), end = '')
print('>')