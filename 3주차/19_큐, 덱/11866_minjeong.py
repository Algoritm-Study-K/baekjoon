<<<<<<< HEAD
from collections import deque
n, k = map(int, input().split())
queue = deque([])

for i in range(1, n + 1):
    queue.append(i)
    
print('<', end='')

while queue:
    for i in range(k - 1):
        queue.append(queue[0])
        queue.popleft()
    print(queue.popleft(), end='')
    if queue:
        print(', ', end='')
        
print('>')
=======
from collections import deque
n, k = map(int, input().split())
queue = deque([])

for i in range(1, n + 1):
    queue.append(i)
    
print('<', end='')

while queue:
    for i in range(k - 1):
        queue.append(queue[0])
        queue.popleft()
    print(queue.popleft(), end='')
    if queue:
        print(', ', end='')
        
print('>')
>>>>>>> 9bfce3ba1e6ddd95a242c42c05eb89b114e96440
