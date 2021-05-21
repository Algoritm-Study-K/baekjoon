import sys
t = sys.stdin.readline().rstrip()
t=int(t)

for _ in range(t):
    a, b = sys.stdin.readline().rstrip().split()
    a=int(a)
    b=int(b)
    print(a+b)