n = int(input())
li = []

for i in range(n):
    [a, b] = map(int, input().split()) # 쌍으로 받기(tuple도 ㄱㅊ)
    li.append([a, b])

li = sorted(li)

for i in range(n):
    print(li[i][0], li[i][1])

