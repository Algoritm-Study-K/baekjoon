T = int(input())

for i in range(T): 
    stack = [] 
    s = input() 
    check = 0 
    for c in s: 
        if c =='(': 
            stack.append(c) 
        elif c ==')': 
            if len(stack) ==0: 
                print('NO') 
                check = 1 
                break 
            else: 
                stack.pop(-1) 

    if len(stack) != 0 and check == 0: 
        print('NO') 
    elif len(stack) ==0 and check ==0: 
        print('YES')