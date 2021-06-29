# 시간초과 주의
# 출처 : https://yuuj.tistory.com/59
# 형태 :  <커서> r_stack

import sys
l_stack = list(sys.stdin.readline().strip()) # 커서 왼쪽 stack
r_stack = [] # 커서 오른쪽 stack
N = int(input())

for _ in range(N):
    str = sys.stdin.readline()
    if str[0] == 'L': # 커서 왼쪽으로 
        if l_stack: 
            r_stack.append(l_stack.pop())
    elif str[0] == 'D': # 커서 오른쪽으로
        if r_stack:
            l_stack.append(r_stack.pop())
    elif str[0] == 'B': # 커서 왼쪽 삭제
        if l_stack:
            l_stack.pop()
    else: # 문자 추가
        l_stack.append(str[2])

print(''.join(l_stack + r_stack[::-1])) # 이거 [::-1안쓰면 시간초과남]