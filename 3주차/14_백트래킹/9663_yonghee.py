def check(i):
	j = 0
	while i > j:
		if board[i] == board[j] or (abs(board[i] - board[j]) == i - j): return False
		j += 1
	return True

def put(i):
	global count
	while board[i] < N:
		if check(i):
			if i == N - 1: count += 1
			else: put(i + 1)
		board[i] += 1
	board[i] = 0

N = int(input())

board = [0] * N
count = 0

put(0)
print(count)