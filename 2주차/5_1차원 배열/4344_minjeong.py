c=int(input())

for i in range(c):
    n=int(input()) #학생 수
    score=[None for i in range(n)]

    score=list(map(int,input().split()))
        
    avg=sum(score)/n

    count=0
    for j in range(n):
        if score[j]>=avg:
            count+=1
    
    ratio = round(count/n,3)
    print(f'{ratio*100}%')
