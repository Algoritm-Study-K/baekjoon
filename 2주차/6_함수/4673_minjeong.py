def s():
    num=set()
    for i in range(1,10001):
        for j in str(i):
            i+=int(j)
        num.add(i)
    return num

ori=set(range(1,10001))
result=ori-s()

for i in sorted(result):
    print(i)
