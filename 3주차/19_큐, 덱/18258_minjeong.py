from collections import deque 

N = int(input()) 
que = deque() 

def push(que, x): 
    que.append(x) 
    
def pop(que): 
    if(not que): 
        return -1 
    else: 
        return que.popleft() 
    
def size(): 
    return len(que) 

def empty(): 
    if(not que): 
        return 1 
    else: 
        return 0 
    
def front(): 
    if(not que): 
        return -1 
    else: 
        return que[0] 
    
def back(): 
    if(not que): 
        return -1 
    else: 
        return que[-1] 
    
for i in range(N): 
    s = input().split() 
    if (s[0] == "push"): 
        push(que, s[1]) 
    elif(s[0] == "pop"): 
        print(pop(que)) 
    elif(s[0] == "size"): 
        print(size()) 
    elif(s[0] == "empty"): 
        print(empty()) 
    elif(s[0] == "front"): 
        print(front()) 
    elif(s[0] == "back"): 
        print(back())