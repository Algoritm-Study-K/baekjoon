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

	def empty(self):
		return not bool(self.stk)

	def clear(self):
		self.stk.clear()


T = int(sys.stdin.readline())

stack = Stack()
for _ in range(T):
	s = sys.stdin.readline()
	for c in s:
		if c == "(":
			stack.push(c)
		elif c == ")":
			if stack.empty():
				print("NO")
				break
			stack.pop()
	else:
		if stack.empty():
			print("YES")
		else:
			print("NO")
	stack.clear()