x = []
num = int(input())

for i in range(num):
    x.append(int(input()))
    
## 간단한 방법
# x.sort()

# bubble sort
for i in range(num-1):
    for j in range(num-1, i, -1):
        if x[j-1] > x[j]:
            x[j-1], x[j] = x[j], x[j-1]

for i in x:
    print(i)