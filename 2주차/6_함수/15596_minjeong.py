n=int(input())

num=0

li=list(str(n))

print(li)
for i in range(1,len(li)):
    if 1<=n<10:
        num+=1
    else:
        if di!=li[i]-li[i-1]:
            break
        di=li[i]-li[i-1]
        num+=1
