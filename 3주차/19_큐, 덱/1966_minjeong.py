test_case = int(input())

for i in range(test_case):
    N, M = map(int,input().split())

    print_list = list(map(int,input().split()))
    check_list = [0 for _ in range(N)] 
    check_list[M] = 1 #문서 위치 저장

    cnt=0
    while True:
        if print_list[0] == max(print_list):
            cnt+=1

            if check_list[0] != 1:
                del print_list[0]
                del check_list[0]
            else:
                print(cnt)
                break
        else:
            print_list.append(print_list[0])
            check_list.append(check_list[0])
            del print_list[0]
            del check_list[0]