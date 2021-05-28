while True:
    s = input()
    if s == '.': #입력 종료
        break

    stack = []
    result = True

    for c in s:
        if c == '(' or c == '[':
            stack.append(c)

        elif c == ')':
            if not stack or stack[-1] == '[':
                result = False
                break
            elif stack[-1] == '(':
                stack.pop()

        elif c == ']':
            if not stack or stack[-1] == '(':
                result = False
                break
            elif stack[-1] == '[':
                stack.pop()
                
    if result == True and not stack:
        print('yes')
    else:
        print('no')