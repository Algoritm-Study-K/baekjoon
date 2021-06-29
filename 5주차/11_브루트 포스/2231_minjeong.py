n = int(input())
res = 0

for i in range(1, n+1):        
    tmp = list(map(int, str(i))) # 분리
    s = i + sum(tmp)   
       
    if(s == n): # 분리합이면       
        res = i                   
        break

print(res)