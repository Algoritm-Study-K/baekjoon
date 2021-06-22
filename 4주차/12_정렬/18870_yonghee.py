N = int(input())

X = list(map(int, input().split()))
X_set = list(sorted(set(X)))

dict = {}

for i in range(len(X_set)):
	dict[X_set[i]] = i

for i in X:
	print(dict[i], end=' ')
print()