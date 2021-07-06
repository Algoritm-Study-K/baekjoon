# 주의 : _666말고 6660 이런 것도 생각해야함!!!!

n = int(input())
res = 666 # 666으로 시작

cnt = 0
while n != 0:
    if '666' in str(res): # 666나오면 카운트 세기
        cnt += 1 

    if cnt == n: # 전체 다 돌면 break
        print(res)
        break
    
    res += 1 # 계속 값++