<<<<<<< HEAD
from collections import deque

N = int(input())
dq = deque()

def empty():
    if len(dq) == 0:
        return 1
    else :
        return 0

for _ in range(N):
    s = list(input().split())
    
    if s[0] == 'push_front':
        dq.appendleft(s[1])

    elif s[0] == 'push_back':
        dq.append(s[1])

    elif s[0] == 'pop_front':
        if empty() == 1:
            print("-1")
        else:
            tmp = dq.popleft()
            print(tmp)

    elif s[0] == 'pop_back':
        if empty() == 1:
            print("-1")
        else:
            tmp = dq.pop()
            print(tmp)

    elif s[0] == 'front':
        if empty() == 1:
            print("-1")
        else:
            print(dq[0])

    elif s[0] == 'back':
        if empty() == 1:
            print("-1")
        else:
            print(dq[len(dq)-1])

    elif s[0] == 'size':
        print(len(dq))
        
    elif s[0] == 'empty':
=======
from collections import deque

N = int(input())
dq = deque()

def empty():
    if len(dq) == 0:
        return 1
    else :
        return 0

for _ in range(N):
    s = list(input().split())
    
    if s[0] == 'push_front':
        dq.appendleft(s[1])

    elif s[0] == 'push_back':
        dq.append(s[1])

    elif s[0] == 'pop_front':
        if empty() == 1:
            print("-1")
        else:
            tmp = dq.popleft()
            print(tmp)

    elif s[0] == 'pop_back':
        if empty() == 1:
            print("-1")
        else:
            tmp = dq.pop()
            print(tmp)

    elif s[0] == 'front':
        if empty() == 1:
            print("-1")
        else:
            print(dq[0])

    elif s[0] == 'back':
        if empty() == 1:
            print("-1")
        else:
            print(dq[len(dq)-1])

    elif s[0] == 'size':
        print(len(dq))
        
    elif s[0] == 'empty':
>>>>>>> 9bfce3ba1e6ddd95a242c42c05eb89b114e96440
        print(empty())