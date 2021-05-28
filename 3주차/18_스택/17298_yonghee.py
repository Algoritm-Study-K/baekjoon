import sys

result = []

N = int(input())

stk = (sys.stdin.readline().split())

for i in range(N):
	for j in range(i + 1, N):
		if stk[j] > stk[i]:
			result.append(stk[j])
			break
	else:
		result.append(-1)

for i in range(N):
	print(result[i], end = ' ')