N = int(input())
for _ in range(N):
	curr = 0
	score = 0
	result = input()
	for s in result:
		if s == 'O':
			curr += 1
			score += curr
		elif s == 'X':
			curr = 0
	print(score)