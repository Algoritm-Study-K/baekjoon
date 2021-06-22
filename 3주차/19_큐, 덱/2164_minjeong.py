<<<<<<< HEAD
from collections import deque 

N = int(input()) 
queue = deque() 

for i in range(N): 
    queue.append(i + 1) 
    
while len(queue) > 1: 
    queue.popleft() 
    queue.append(queue.popleft()) 
    
=======
from collections import deque 

N = int(input()) 
queue = deque() 

for i in range(N): 
    queue.append(i + 1) 
    
while len(queue) > 1: 
    queue.popleft() 
    queue.append(queue.popleft()) 
    
>>>>>>> 9bfce3ba1e6ddd95a242c42c05eb89b114e96440
print(queue.pop())