import sys
n = int(sys.stdin.readline())

li = [0] * n

for i in range(n):
    li[int(sys.stdin.readline())] += 1

for i in range(n):
    if li[i] != 0:
        for j in range(li[i]):
            print(i)