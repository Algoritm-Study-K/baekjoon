#인터넷 보고 함
alpa = list(map(int, input().split()))
a = [1, 2, 3, 4, 5]

while True:
    for i in range(len(alpa)-1):
        if alpa[i] > alpa[i+1]:
            alpa[i], alpa[i+1] = alpa[i+1], alpa[i]
            print(" ".join(map(str, alpa)))

    if alpa == a:
        break