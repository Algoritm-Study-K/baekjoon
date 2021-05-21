a=[None]*10
for i in range(10):
    a[i]=int(input())
    a[i]%=42

b=[None]*10
r=0
for i in range(10):
    if a[i] not in b:
        b[r]=a[i]
        r+=1
#print(b)
print(r)
