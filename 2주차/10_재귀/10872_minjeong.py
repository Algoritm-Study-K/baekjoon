def fac(n):
    if n==1:
        return 1 #여기에 1반환해줘야 n*n-1*...*2*1 형태 맞춰짐!
    return n*fac(n-1)

n=int(input())
if n==0: #0일 때에는 1로 예외 출력
    print(1)
else:
    print(fac(n))