from itertools import combinations

n, m = map(int, input().split())
C = combinations(range(1, n+1), m) #조합

for i in C:
    print(' '.join(map(str, i)))