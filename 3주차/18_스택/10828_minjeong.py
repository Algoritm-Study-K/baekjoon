#함수로 따로 빼서 만들기

N = int(input().rstrip())
stack = []

for _ in range(N):
    input_str = input().rstrip().split()
    order = input_str[0]

    if order == "push":
        stack.append(input_str[1])

    elif order == "pop":
        if(not stack):
            print(-1)
        else:
            print(stack.pop())

    elif order == "size":
        print(len(stack))

    elif order == "empty":
        if stack:
            print(0)
        else:
            print(1)

    elif order== "top":
        if stack:
            print(stack[1])
        else:
            print(-1)