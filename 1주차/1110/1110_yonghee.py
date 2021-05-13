N = int(input())

i = N
count = 0
while True:
	i = (i % 10) * 10 + (i // 10 + i % 10) % 10
	count += 1
	if i == N:
		break
print(count)