import sys
a, b = sys.stdin.readline().rstrip().split()
a = int(a)
b = int(b)

if a>b:
    print('>')
elif a<b:
    print('<')
else:
    print('==')