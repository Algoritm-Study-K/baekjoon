import sys

class Stack:
	def __init__(self):
		self.stk = []

	def push(self, value):
		self.stk.append(value)

	def pop(self):
		if not self.stk:
			print(-1)
		else:
			print(self.stk.pop())

	def size(self):
		print(len(self.stk))
	
	def empty(self):
		if self.stk:
			print(0)
		else:
			print(1)

	def top(self):
		if not self.stk:
			print(-1)
		else:
			print(self.stk[-1])

N = int(input())

stack = Stack()

for _ in range(N):
	s = sys.stdin.readline().split()
	if s[0] == 'push':
		stack.push(s[1])
	elif s[0] == 'pop':
		stack.pop()
	elif s[0] == 'size':
		stack.size()
	elif s[0] == 'empty':
		stack.empty()
	elif s[0] == 'top':
		stack.top()