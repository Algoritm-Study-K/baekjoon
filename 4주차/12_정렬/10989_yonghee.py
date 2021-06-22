from sys import stdin
N = int(input())
f = [0] * 10001

for i in range(N):
	num = int(stdin.readline())
	f[num] += 1

for i in range(10001):
	if f[i] > 0:
		for _ in range(f[i]):
			print(i)