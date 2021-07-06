n, m = map(int, input().split())
card = list(map(int,input().split()))

res = 0
for i in range(n-2): # 앞 카드 pick
    for j in range(i+1, n-1): # 중간 카드 pick
        for k in range(j+1, n): # 마지막 카드 pick
            if (card[i]+card[j]+card[k]) <= m:
                if (card[i]+card[j]+card[k]) > res:
                    res = card[i]+card[j]+card[k]

print(res)