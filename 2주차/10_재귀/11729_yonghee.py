def hanoi(N, p1, p2, p3):
	if N == 1:
		print(p1, p3)
	else:
		hanoi(N - 1, p1, p3, p2)
		print(p1, p3)
		hanoi(N - 1, p2, p1, p3)
N = int(input())
print(2 ** N - 1)
hanoi(N, 1, 2, 3)