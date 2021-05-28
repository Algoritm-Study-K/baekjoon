class Queue():
	def __init__(self, size):
		self.que = [i for i in range(1, size + 1)]
		self.count = size
		self.result = 0

	def move_left(self):
		self.que.append(self.que.pop(0))
		self.result += 1

	def move_right(self):
		self.que.insert(0, self.que.pop())
		self.result += 1

	def dequeue(self):
		if not self.que:
			return -1
		else:
			self.que.pop(0)
			self.count -= 1

N, M = map(int, input().split())
num = list(map(int, input().split()))

queue = Queue(N)

for i in range(M):
	while True:
		if queue.que[0] == num[i]:
			queue.dequeue()
			break
		elif queue.que.index(num[i]) > queue.count // 2:
			queue.move_right()
		elif queue.que.index(num[i]) <= queue.count // 2:
			queue.move_left()

print(queue.result)