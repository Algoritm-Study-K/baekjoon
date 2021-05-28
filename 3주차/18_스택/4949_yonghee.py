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


stack = Stack()
while(True):
	s = sys.stdin.readline()
	if s == '.\n':
		break
	for c in s:
		if c == "(" or c == "[":
			stack.push(c)
		elif c == ")":
			if stack.empty():
				print("no")
				break
			elif stack.stk[-1] == "(":
				stack.pop()
			else:
				print("no")
				break
		elif c == "]":
			if stack.empty():
				print("no")
				break
			elif stack.stk[-1] == "[":
				stack.pop()
			else:
				print("no")
				break

	else:
		if stack.empty():
			print("yes")
		else:
			print("no")
	stack.clear()
