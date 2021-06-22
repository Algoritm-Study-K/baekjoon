## input쓰면 시간초과

import sys
num = int(input())
x = []

for i in range(num):
    x.append(int(sys.stdin.readline()))
    
x.sort()

for i in x:
    print(i)