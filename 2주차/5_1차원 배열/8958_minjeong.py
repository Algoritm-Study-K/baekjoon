n=int(input())
case=[None]*n #case 갯수 입력

for i in range(n):
    ipt=input() #OX입력
    score=0
    result=0
    for j in ipt:
        if j=='O':
            score+=1
        else:
            score=0
        result+=score
    print(result)
