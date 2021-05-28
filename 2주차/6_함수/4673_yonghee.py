numbers = set(range(1, 10001))
not_self_number = set()

for i in range(1, 10000):
	sum = 0
	sum += i
	while (i > 0):
		sum += i % 10
		i = i // 10
	not_self_number.add(sum)

self_number = sorted(numbers - not_self_number)
for i in self_number:
	print(i)