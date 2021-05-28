import sys
from collections import deque
class Queue():
	def __init__(self):
		self.items = deque()
		self.count = 0

	def push(self, X):
		self.items.append(X)
		self.count += 1

	def pop(self):
		if self.count == 0:
			print(-1)
		else:
			print(self.items.popleft())
			self.count -= 1
	
	def size(self):
		print(self.count)

	def empty(self):
		if self.count == 0:
			print(1)
		else:
			print(0)

	def front(self):
		if self.count == 0:
			print(-1)
		else:
			print(self.items[0])

	def back(self):
		if self.count == 0:
			print(-1)
		else:
			print(self.items[-1])

N = int(input())

queue = Queue()

for _ in range(N):
	str = sys.stdin.readline().split()
	if str[0] == "push":
		queue.push(str[1])
	elif str[0] == "pop":
		queue.pop()
	elif str[0] == "size":
		queue.size()
	elif str[0] == "empty":
		queue.empty()
	elif str[0] == "front":
		queue.front()
	elif str[0] == "back":
		queue.back()