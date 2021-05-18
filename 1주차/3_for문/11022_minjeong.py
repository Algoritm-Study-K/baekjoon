import sys
t = sys.stdin.readline().strip()
t = int(t)

for i in range(1, t+1):
    a, b = sys.stdin.readline().strip().split()
    a = int(a)
    b = int(b)
    print(f'Case #{i}: {a} + {b} = {a+b}')