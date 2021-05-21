a=int(input())
b=int(input())
c=int(input())

r=a*b*c
list_r=list(str(r)) #int->string->list변환

add=[0]*10
for i in range(len(list_r)):
    add[int(list_r[i])]+=1

#print(add)
for i in range(10):
    print(add[i])