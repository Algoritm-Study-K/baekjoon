import collections
n, m = map(int, input().split()) # 큐의 크기, 뽑는 갯수
where = list(map(int, input().split())) # 위치
result = 0
que = collections.deque([i for i in range(1, n +1)]) # n사이즈로 큐 제작

for num in where: # 뽑는 위치 확인
    if num == que[0]: # 맨 앞에 있으면 바로 뽑음
        que.popleft() 
        continue

    # 왼쪽/오른쪽 중 어디에 더 가까운 지 계산
    left = que.index(num)
    right = len(que) - left
    
    if left <= right: # 왼쪽에 더 가까울 때
        que.rotate(-left) # 오른쪽 방향이 default라서
        que.popleft()
        result += left

    else: # 오른쪽에 더 가까울 때
        que.rotate(right)
        que.popleft() 
        result += right
        
print(result)