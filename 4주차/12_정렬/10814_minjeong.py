n = int(input())
li = []

for i in range(n):
    age, name = map(str, input().split())
    age = int(age)
    li.append((age, name))

## lamda 써줘야함!!! 안쓰고 간단한 방법 못찾음ㅠ
li.sort(key = lambda x : x[0])	## age만 비교

for i in li:
    print(i[0], i[1])