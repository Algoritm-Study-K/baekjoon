import sys

class Stack:
	def __init__(self):
		self.stk = []

	def push(self, value):
		self.stk.append(value)

	def pop(self):
		if not self.stk:
			return(-1)
		else:
			return(self.stk.pop())

K = int(input())

stack = Stack()

for _ in range(K):
	n = int(sys.stdin.readline())
	if n == 0:
		stack.pop()
	else:
		stack.push(n)
print(sum(stack.stk))