## input쓰면 시간 초과
import sys
from collections import Counter

n = int(sys.stdin.readline())
num = []

for i in range(n):
    num.append(int(sys.stdin.readline()))
num.sort()

print(round(sum(num)/n)) # 산술 평균
print(num[n//2]) # 중앙값

many = Counter(num).most_common()
if len(many) > 1: # 최빈값 : most common 써서...
    if many[0][1] == many[1][1]:
        print(many[1][0])
    else:
        print(many[0][0])
else:
    print(many[0][0])

print(num[n-1] - num[0]) # 범위 : 마지막-첫번째