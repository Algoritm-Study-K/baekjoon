n = int(input())

time = 0
tmp = n
while(True):
    first = tmp%10
    ten = tmp//10
    sum = ten + first
    #print(f'{ten}+{first}={sum}')
    new = first*10 + sum%10
    time += 1

    if (n==new): break
    tmp = new

print(time)