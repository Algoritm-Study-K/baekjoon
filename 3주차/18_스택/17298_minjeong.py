N = int(input()) 
input_list = list(map(int, input().split())) 

stack = [] 
result = [-1 for _ in range(N)] 
stack.append(0) 
i = 1 

while stack and i < N: 
    while stack and input_list[stack[-1]] < input_list[i]: 
        result[stack[-1]] = input_list[i] 
        stack.pop() 
    stack.append(i) 
    i += 1 
    
for i in range(N): 
    print(result[i], end = " ") 