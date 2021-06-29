n, k = map(int, input().split())
people = list(range(1, n+1)) # 번호 붙인 리스트
result = []

i = k-1
while True:
    result.append(people.pop(i))
    if len(people) == 0: # 리스트에 아무것도 없으면
        break
    i = (i+k-1) % len(people)

print('<' + ', '.join(map(str, result)) + '>') # 한 줄에 출력