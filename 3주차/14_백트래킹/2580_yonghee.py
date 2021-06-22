board = [list(map(int, input().split())) for _ in range(9)]
zeros = [(i, j) for i in range(9) for j in range(9) if board[i][j] == 0]

count = 0
for row in board:
	for i in row:
		if i == 0:
			count += 1

def check(n, i, j):
	for y in range(9):
		if board[i][y] == n:
			return False
	for x in range(9):
		if board[x][j] == n:
			return False
	for x in range(3):
		for y in range(3):
			if n == board[i // 3 * 3 + x][j // 3 * 3 + y]:
				return False
	return True

def put(n):
	if n == count:
		for row in board:
			for n in row:
				print(n, end=' ')
			print()
		return
	else:
		pass