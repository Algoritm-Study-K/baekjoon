import sys
from collections import deque

K = int(input())
for _ in range(K):
	N, M = map(int, (sys.stdin.readline().split()))
	queue = deque()
	prior = deque(map(int, sys.stdin.readline().split()))
	count = 0
	for i in range(N):
		queue.append(i)
	while True:
		if prior[0] == max(prior):
			count += 1
			if queue[0] == M:
				print(count)
				break
			else:
				queue.popleft()
				prior.popleft()
		else:
			queue.append(queue.popleft())
			prior.append(prior.popleft())
