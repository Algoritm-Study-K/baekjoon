def stars(size, i, j):
	if size == 1:
		stars_map[i][j] = '*'
	else:
		size //= 3
		for a in range(3):
			for b in range(3):
				if (a, b) == (1, 1):
					continue
				stars(size, i + size * a, j + size * b)

N = int(input())
stars_map = [[' ' for _ in range(N)] for _ in range(N)]
stars(N, 0, 0)
for line in stars_map:
	print(''.join(line))