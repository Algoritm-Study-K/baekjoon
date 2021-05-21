def solve(a):
    ans=0
    if a<100: #1,2자리수는 모두 한수임
        ans+=1
    else:
        numli=list(map(int,str(a))
        if numli[0]-numli[1]==numli[1]-numli[2]:
            ans+=1

    return ans

n=int(input())
print(solve(n))

#에러 왜 뜨는걸까...?