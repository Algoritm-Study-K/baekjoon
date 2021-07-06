n = int(input())

p = []
for i in range(n): # 키,몸무게 입력받기
    weight, height = map(int, input().split())
    p.append((weight,height))

for me in p: # 나 
    rank = 1
    for other in p: # 상대방
        if me[0] != other[0] and me[1] != other[1]: # 조건이 똑같을 때
            if me[0] < other[0] and me[1] < other[1]: # 상대 조건이 더 좋을 때
                rank += 1

    print(rank, end=' ')