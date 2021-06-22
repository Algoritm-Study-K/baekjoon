import sys
n = int(sys.stdin.readline())
li = list(map(int,sys.stdin.readline().split()))

li_aft = []
li_aft = list(sorted(set(li)))

# {key:value}형태로 저장
dic = {li_aft[i]: i for i in range (len(li_aft))}

for i in li:
    print(dic[i],end=' ')

