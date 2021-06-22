N = input()
n = []
for i in N:
	n.append(int(i))

for s in sorted(n, reverse=True):
	print(s, end='')
print()