num=[None]*9
for i in range(9):
    num[i]=int(input())

print(max(num))
print(num.index(max(num))+1) #+1해야하는 것 주의하기