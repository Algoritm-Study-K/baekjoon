import sys

N = int(sys.stdin.readline())

deque = []

def push_back(x):
	deque.append(x)

def push_front(x):
	deque.insert(0, x)

def pop_front():
	if not deque:
		print(-1)
	else:
		print(deque.pop(0))

def pop_back():
	if not deque:
		print(-1)
	else:
		print(deque.pop())

def size():
	print(len(deque))

def empty():
	if not deque:
		print(1)
	else:
		print(0)

def front():
	if not deque:
		print(-1)
	else:
		print(deque[0])

def back():
	if not deque:
		print(-1)
	else:
		print(deque[-1])

for i in range(N):
	str = sys.stdin.readline().split()
	if str[0] == 'push_front':
		push_front(str[1])

	elif str[0] == 'pop_front':
		pop_front()

	if str[0] == 'push_back':
		push_back(str[1])

	elif str[0] == 'pop_back':
		pop_back()

	elif str[0] == 'size':
		size()

	elif str[0] == 'empty':
		empty()

	elif str[0] == 'front':
		front()

	elif str[0] == 'back':
		back()
