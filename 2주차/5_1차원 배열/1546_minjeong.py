n=int(input())
score=list(map(int, input().split()))

max_s=max(score)
for i in range(len(score)):
    score[i]=score[i]/max_s*100

print(sum(score)/n)