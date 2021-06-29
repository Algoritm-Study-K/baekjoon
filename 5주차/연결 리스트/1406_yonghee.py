import sys

str = list(sys.stdin.readline().strip())
M = int(input())
cursor = len(str)

for i in range(M):
	command = sys.stdin.readline()
	if command[0] == 'L':
		if cursor != 0:
			cursor -= 1
	elif command[0] == 'D':
		if cursor != len(str):
			cursor += 1
	elif command[0] == 'B':
		if cursor != 0:
			del str[cursor - 1]
			cursor -= 1
	elif command[0] == 'P':
		str.insert(cursor, command[2])
		cursor += 1
print("".join(str))
