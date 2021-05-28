n = int(input())
s = []
result = []
cnt = 1
temp = True

for i in range(n):
    num = int(input())
    while cnt <= num:
        s.append(cnt)
        result.append('+')
        cnt += 1
    if s[-1] == num:
        s.pop()
        result.append('-')
    else:
        temp = False

if temp == False:
    print('NO')
else:
    for i in result:
        print(i)
