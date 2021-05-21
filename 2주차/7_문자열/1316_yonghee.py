N = int(input())
count = 0

for i in range(N):
	word = input()
	prev = word[0]
	letters = [prev]
	for c in word[1:]:
		if c in letters and c == prev:
			continue
		elif c not in letters and c != prev:
			letters.append(c)
			prev = c
		else:
			break
	else:
		count += 1
print(count)