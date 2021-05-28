import sys

class Stack:
	def __init__(self):
		self.stk = []
		self.result = []
		self.count = 0

	def push(self, value):
		self.stk.append(value)
		self.result.append('+')
		self.count += 1

	def pop(self):
		if not self.stk:
			return(-1)
		else:
			self.result.append('-')
			return(self.stk.pop())

	def empty(self):
		return not bool(self.stk)

n = int(input())

stack = Stack()
impossible = 0
for i in range(n):
	num = int(sys.stdin.readline())
	while stack.count <= n:
		if stack.empty() and stack.count < n:
			stack.push(stack.count + 1)
		elif not stack.empty() and stack.stk[-1] > num:
			stack.pop()
		elif not stack.empty() and stack.stk[-1] == num:
			stack.pop()
			break
		elif stack.count < n:
			stack.push(stack.count + 1)
		else:
			impossible = 1
			break
if impossible:
	print("NO")
else:
	for i in range(len(stack.result)):
		print(stack.result[i])