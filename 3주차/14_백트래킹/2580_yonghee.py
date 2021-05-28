board = [list(map(int, input().split())) for _ in range(9)]
count = 0
for row in board:
	for i in row:
		if i == 0:
			count += 1

def check(n, i, j):
	if n in board[i]:
		return False
	for x in range(9):
		if board[x][j] == n:
			return False
	for x in range(3):
		for y in range(3):
			if n == board[i // 3 * 3 + x][j // 3 * 3 + y]:
				return False

def put(n):
	if n == count:
		pass