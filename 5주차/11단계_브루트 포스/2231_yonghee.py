N = int(input())
for i in range(N):
	sum = i
	for s in str(i):
		sum += int(s)
	if sum == N:
		print(i)
		break
else:
	print(0)